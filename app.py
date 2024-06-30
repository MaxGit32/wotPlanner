import tkinter 
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from functools import partial

def main():
    global map_dropdown, mode_dropdown, canvas, mapImage, markType, markImages, mark_ids, imageSizeX, imageSizeY

    app = tkinter.Tk()
    app.title("WoT Strategy-Planner")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    geometry = str(screen_width) + "x" + str(screen_height)
    app.geometry(geometry) 
    screen_height = app.winfo_screenheight()
    screen_width = app.winfo_screenwidth()

    bgImageTk = ImageTk.PhotoImage(file="./Images/WotBackground.jpeg")
    
    canvas = tkinter.Canvas(app, width=screen_width, height=screen_height)
    canvas.create_image(0, 0, anchor='nw' ,image=bgImageTk)
    canvas.create_text(35,25, text='Maps', fill='black', font=('times',15))
    canvas.pack(fill="both", expand=True)    

    canvas.bind("<Button-1>", drawMark)

    mapList = ['Abbey','Airfield','Cliff','El Haluf','Empires Border','Ensk','Erlenberg','Fisherman\'s Bay','Fjords','Ghost Town','Glacier',
    'Highway','Himmelsdorf','Karelia','Klondike','Kraftwerk','Lakeville','Live Oaks','Malinovka','Mannerheim Line','Mines','Mountain Pass',
    'Murovanka','Nebelburg','Normandie','Overlord','Paris','Pilsen','Prohorovka','Province','Redshire','Ruinberg','Sand River','Serenecoast',
    'Siegfried Line','Steppes','Studzianki','Tundra','Westfield','Widepark']

    map_dropdown = ttk.Combobox(app, values=mapList)
    map_dropdown.place(x=10, y=40)
    map_dropdown.bind("<<ComboboxSelected>>", on_map_selected)

    modeList = ['Standard', 'Encounter', 'Assault']
    mode_dropdown = ttk.Combobox(app, values=modeList)
    mode_dropdown.place(x=200, y=40)
    mode_dropdown.bind("<<ComboboxSelected>>", on_map_selected)

    #Buttons
    x = 10
    y = 80

    sizes = ["1", "2", "3"]
    for size in sizes:
        button = tkinter.Button(app, text=size, command=partial(selectImageSize, size))
        button.place(x=x,y=y)
        x+=100
    x-=(300)
    y+=40

    ally_button_names = ["Ally Light", "Ally Medium", "Ally Heavy", "Ally Tankdestroyer", "Ally Self-Propelled"]
    enemy_button_names = ["Enemy Light", "Enemy Medium", "Enemy Heavy", "Enemy Tankdestroyer", "Enemy Self-Propelled"]
    
    for name in ally_button_names:
        button = tkinter.Button(app, text=name, command=partial(selectMarkType, name))
        button.place(x=x,y=y)
        y+= 40

    for name in enemy_button_names:
        button = tkinter.Button(app, text=name, command=partial(selectMarkType, name))
        button.place(x=x,y=y)
        y+=40
    
    button = tkinter.Button(app, text="Delete", command=partial(deleteMark))
    button.place(x=x,y=y)
    y+=40

    button = tkinter.Button(app, text="Delete All", command=partial(deleteAllMarks))
    button.place(x=x,y=y)

    markType = None

    markImages = []
    mark_ids = []

    app.mainloop()

def on_map_selected(event):
    global map_dropdown, mode_dropdown, selectedMap

    selectedMapName = map_dropdown.get()
    selectedMode = mode_dropdown.get()
    selectedMap = selectedMapName + selectedMode
    if selectedMap:
        fetch_and_display_map(selectedMap.lower().strip())

def fetch_and_display_map(map):
    global canvas, mapImage

    response = fetchMap(map)
    if len(response) == 0:
        mapImage = Image.open('./maps/noMap.png')
        mapImage = mapImage.resize((800, 800), Image.LANCZOS)
        mapImage = ImageTk.PhotoImage(mapImage)
        canvas.create_image(0.5 * canvas.winfo_width(), 0.5 * canvas.winfo_height(), anchor=tkinter.CENTER, image=mapImage)
    
    if len(response) > 0:
        mapURL = response[0].get('url')
        mapImage = Image.open(mapURL)
        mapImage = mapImage.resize((800, 800), Image.LANCZOS)
        mapImage = ImageTk.PhotoImage(mapImage)
        canvas.create_image(0.5 * canvas.winfo_width(), 0.5 * canvas.winfo_height(), anchor=tkinter.CENTER, image=mapImage)
        
def fetchMap(map):
    response = requests.get("http://localhost:3000/maps?mapname=eq.{}".format(map))
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch map.")
        return None

def selectMarkType(selectedMarkType):
    global markType

    markType = selectedMarkType.replace(" ", "")

def selectImageSize(size):
    global imageSizeX, imageSizeY
    if int(size) == 3:
        imageSizeX = 30
        imageSizeY = 30
    if int(size) == 2:
        imageSizeX = 20
        imageSizeY = 20
    if int(size) == 1:
        imageSizeX = 10
        imageSizeY = 10

def drawMark(event):
    global markType, canvas, markImages, mark_ids,selectedMap, imageSizeX, imageSizeY

    if markType is None or selectedMap is None:
        return 

    x, y = event.x, event.y
    markImage = Image.open('./Images/{}.png'.format(markType))
    markImage = markImage.resize((imageSizeX, imageSizeY), Image.LANCZOS)
    markImage = ImageTk.PhotoImage(markImage)
    markImages.append(markImage)
    mark_id = canvas.create_image(x, y, anchor=tkinter.CENTER, image=markImage)
    mark_ids.append(mark_id)

def deleteMark(event):
    x, y = event.x, event.y
    

def deleteAllMarks():
    global canvas, mark_ids, markImages

    for mark_id in mark_ids:
        canvas.delete(mark_id)
    mark_ids.clear()
    markImages.clear()


if __name__ == "__main__":
    main()