from utilities import fonction, token
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

description = """
API Emergency Projet Scientifique Transverse 🚒

## Projet

Github: <a href="https://github.com/ProjetScientifique">Github 💻</a>  
Trello: <a href="https://trello.com/b/U4bDVtQ6/projet-transversal">Trello Projet 📈</a>

## Utilisation API:

Vous devez posseder le token de l'api  


## Token 🔑 :
### CB814D37E278A63D3666B1A1604AD0F5C5FD7E177267F62B8D719F49182F410A

"""

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Emergency",
    description=description,
    version="0.0.1",
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["DEBUG"])
def interfaceAPI():
    return {"API Emergency": "Groupe 1"}

