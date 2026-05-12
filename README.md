# To-Do API - Lavet med FastAPI

API’et er et simpelt in-memory To-Do API bygget med FastAPI. Det gør det muligt at oprette, hente og slette to-do opgaver.
Hver opgave får automatisk et ID, og data nulstilles når serveren genstartes.
Når alle to-do opgaver er slettet fra listen, nulstilles tælleren - dvs. at to-do opgaver oprettet derefter, vil starte på todo_id = 1

Efter udført research, valgte jeg at gå med FastAPI, da denne automatisk opsætter Swagger UI.

API’et gør det muligt at:
* Oprette to-do opgaver
* Vise alle to-do opgaver
* Slette to-do opgaver via ID

Data gemmes i en liste i hukommelsen. Dvs. at alt indtastet data nulstilles/fjernes, når programmet genstartes.

### Start server:
uvicorn main:app --reload

### Åbn API dokumentation:
http://127.0.0.1:8000/docs

### Docker
Build:
docker build -t todo-api .

### Kør:
docker run -p 8000:8000 todo-api

### Installer dependencies:
pip install -r requirements.txt

## Anvendte dependencies
- Python
- FastAPI
- Uvicorn
- Docker

### Lavet af
Marco Giorgio A. Hillemann
IT-Teknolog studerende (Erhvervsakademi København)
