Die .sql Datein im Verzeichnis init-db.d werden bei docker-compose up aufgrund der Zeilen 

volumes:
      - ./init-db.d:/docker-entrypoint-initdb.d

zum Initialisieren der PostgreSQL-Containers genutzt, wenn kein Verzeichnis "data" vorliegt.
--> data-Verzeichnis löschen: sudo rm -rf pathTodata/data

PostgREST ermöglicht es im .json Format alle Relationen, Views, Funktionen,... aus dem PostgreSQL-Container abzufragen.
Mit JavaScript: fetch-Befehl (GET (SELECT), POST (INSERT),...)
--> Testen des PostgREST-Server: curl http://localhost:3000/maps?mapname=eq.abbey
- jwt Key muss min. 32 Stellen lang sein
- PostGREST loggt sich mit user ein, der im Payload steht, daher muss user Rechte haben, um DB abzufragen

TEST:
curl -X POST "http://localhost:3000/rpc/register_user"      -H "Content-Type: application/json"      -d '{"_username": "user", "_password": "pass"}'
curl -X POST "http://localhost:3000/rpc/register_user"      -H "Content-Type: application/json"      -d '{"_username": "user", "_password": "pass"}'

LOGIN mit psql:
psql -h localhost -U max -d wot-planer

