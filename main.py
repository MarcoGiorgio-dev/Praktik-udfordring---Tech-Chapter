# Starter FastAPI og opretter API’et
from fastapi import FastAPI
app = FastAPI()

# todos = liste med opgaver
# counter = giver nye ID’er
todos = []
counter = 1

# Returnerer alle to-dos
@app.get("/todos")
def get_todos():

    # Printer hvad der sker i terminalen
    print("GET /todos kaldt")
    print(todos)

    return todos

# Modtager en ny to-do fra Swagger og logger den
@app.post("/todos")
def create_todo(todo: dict):

    # Gør det muligt at ændre ID-tælleren inde i en funktion
    global counter
    print("POST /todos kaldt")

    # Giver to-do opgaven et ID og øger tælleren med 1
    print("Input:", todo)
    todo["id"] = counter
    counter += 1

    # Gemmer to-do'en i listen
    todos.append(todo)

    # Logger input of listen i terminalen
    print("Gemte todos:", todos)

    return {"message": "To-do oprettet!", "Nyt punkt: ": todo}

# Opretter en funktion der sletter en to-do baseret på ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    print(f"DELETE /todos/{todo_id} kaldt")
    global counter
    for todo in todos:

        # Finder den korrekte to-do
        if todo["id"] == todo_id:
            todos.remove(todo)
            print("Slettet:", todo)
            print("Resterende todos:", todos)

            # Nulstiller ID hvis listen er tom
            if len(todos) == 0:
                counter = 1

            return {"message": "To-do slettet", "todo": todo}
    print("Ikke fundet")

    return {"error": "Opgave ikke fundet"}
