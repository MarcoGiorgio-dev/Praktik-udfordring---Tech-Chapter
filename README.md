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




# Sådan køres projektet lokalt ---------- Denne del er skrevet for min egen skyld, til fremtidig reference/repetition

### Docker opsætning (kort guide):

1. Sørg for at Docker Desktop er installeret og kører
2. Byg image:
   docker build -t todo-api .
3. Kør container:
   docker run -p 8000:8000 todo-api
4. Åbn API i browser:
   http://localhost:8000/docs

### Oprettelse af virtuel miljø (venv) i VS Code:

1. Åbn projektmappen i VS Code
2. Åbn terminalen (Ctrl + `)
3. Opret venv:
   python -m venv venv
4. Aktivér venv:
   venv\Scripts\activate (Windows)
5. Vælg interpreter i VS Code:
   Ctrl + Shift + P → "Python: Select Interpreter" → vælg venv

# Bemærk
Projektet er lavet som en læringsopgave, og bruger ikke database.

Input i POST funktionen på Swagger UI skal skrives således:
  Eksempel 1:
  {
  "title": "Lav praktikudfordringsopgaven fra Tech Chapter",
  "done": true
  }

  Eksempel 2:
  {
  "title": "Giv op når det driller",
  "done": false
  }
