import tkinter 
from tkinter import ttk
from PIL import Image, ImageTk
def main():
    global map_dropdown
    app = tkinter.Tk()
    app.title("WoT Strategy-Planner")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    geometry = str(screen_width) + "x" + str(screen_height)
    app.geometry(geometry) 
    screen_height = app.winfo_screenheight()
    screen_width = app.winfo_screenwidth()

    bgImageTk = ImageTk.PhotoImage(file="./resources/Images/WotBackground.jpeg")
    
    canvas = tkinter.Canvas(app, width=screen_width, height=screen_height)
    canvas.create_image(0, 0, anchor='nw' ,image=bgImageTk)
    canvas.create_text(35,25, text='Maps', fill='black', font=('times',15))
    canvas.pack(fill="both", expand=True)    

    mapList = ['Abbey']
    map_dropdown = ttk.Combobox(app, values=mapList)
    map_dropdown.place(x=10, y=40)
    map_dropdown.bind("<<ComboboxSelected>>", showMap)

    app.mainloop()

def showMap(event):
    global map_dropdown
    selectedMap = map_dropdown.get()
    print(f"Selected Map: {selectedMap}")


if __name__ == "__main__":
    main()