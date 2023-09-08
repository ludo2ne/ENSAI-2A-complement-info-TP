from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


@app.get("/hello")
async def get_hello():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def get_hello_name(name: str):
    return {"message": "Hello {}".format(name)}


# Define a Pydantic model for the character
class Personnage(BaseModel):
    nom: str
    age: int


# Create a dictionary to store characters
characters_db: Dict[int, Personnage] = {}
characters_db[1] = Personnage(nom="Anne", age=33)
characters_db[2] = Personnage(nom="Michel", age=20)
character_id = 3  # Initial character ID


# Add a character
@app.post("/character/")
def create_character(character: Personnage):
    global character_id
    characters_db[character_id] = character
    character_id += 1
    return character


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
