from utilities import fonction, token
from typing import List, Optional

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

"""===============
SAME AS SIMULATION
==============="""


"""
.___                                .___.__        
|   | ____   ____  ____   ____    __| _/|__| ____  
|   |/    \_/ ___\/ __ \ /    \  / __ | |  |/ __ \ 
|   |   |  \  \__\  ___/|   |  \/ /_/ | |  \  ___/ 
|___|___|  /\___  >___  >___|  /\____ | |__|\___  >
         \/     \/    \/     \/      \/         \/ 
"""

"""POST  REQUESTS"""
@app.post("/incident/", tags=["Incident"], response_model=schemas.Incident)
def nouvel_incident(token_api: str, incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    """
        Adding a new incident dans la base de donnée.</br>
        Les incidents on a besoin de:</br>
            - intensite</br>
            - latitude</br>
            - longitude</br>

        Exemple d'utilisation:
        POST: localhost:8000/new/incident?token="token",detecteur="1",intensite="10",latitude="45.76275055566161",longitude="4.844640087180309"
        <!--
        Python :

        :param token_api: str
        :param detecteur: str
        :param intensite: str
        :param latitude: str
        :param longitude: str
        :return: json response.
        -->
        """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_incidents(db, incident=incident)


"""GET  REQUESTS"""
@app.get("/incident/{incident_id}", tags=["Incident"], response_model=schemas.IncidentAll)
def get_Incident(token_api: str, incident_id: int, db: Session = Depends(get_db)):
    """
    Récupères tous les incidents dans une table.
    :return:
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    db_incident = crud.get_incident(db, incident_id=incident_id)
    if db_incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return db_incident


@app.get("/incidents/", tags=["Incident"], response_model=List[schemas.IncidentAll])
def get_Incidents(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Récupères tous les incidents dans une table.
    :return:
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incidents = crud.get_incidents(db, skip=skip, limit=limit)
    return incidents


"""PATCH REQUESTS"""


@app.patch("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def edit_incident(incident_id: int, token_api: str, incident: schemas.IncidentUpdate, db: Session = Depends(get_db)):
    """
        PATCH = met a jour uniquement certaines données
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incident_to_edit = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()
    if incident.id_type_incident: incident_to_edit.id_type_incident = incident.id_type_incident
    if incident.latitude_incident: incident_to_edit.latitude_incident = incident.latitude_incident
    if incident.longitude_incident: incident_to_edit.longitude_incident = incident.longitude_incident
    if incident.intensite_incident: incident_to_edit.intensite_incident = incident.intensite_incident
    if incident.date_incident: incident_to_edit.date_incident = incident.date_incident
    if incident.id_type_status_incident: incident_to_edit.id_type_status_incident = incident.id_type_status_incident


    db.commit()
    return incident_to_edit


"""PUT REQUESTS"""


@app.put("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def change_incident(incident_id: int, incident: schemas.IncidentCreate, token_api: str, db: Session = Depends(get_db)):
    """
        PUT = réécrit
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incident_to_edit = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()
    incident_to_edit.latitude_incident = incident.latitude_incident
    incident_to_edit.longitude_incident = incident.longitude_incident
    incident_to_edit.intensite_incident = incident.intensite_incident
    incident_to_edit.date_incident = incident.date_incident
    incident_to_edit.id_type_status_incident = incident.id_type_status_incident

    db.commit()

    return incident_to_edit


"""DELETE REQUESTS"""


@app.delete("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def delete_incident(incident_id: int, token_api: str, db: Session = Depends(get_db)):
    """
        PUT = réécrit

        """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incident_delete = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()

    if incident_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(incident_delete)
    db.commit()

    return incident_delete


"""
_________                __                       
\_   ___ \_____  _______/  |_  ____  __ _________ 
/    \  \/\__  \ \____ \   __\/ __ \|  |  \_  __ \
\     \____/ __ \|  |_> >  | \  ___/|  |  /|  | \/
 \______  (____  /   __/|__|  \___  >____/ |__|   
        \/     \/|__|             \/              
"""

"""
POST Request
    - Good à tester.
"""


@app.post("/detecteur/", tags=["Detecteur"], response_model=schemas.Detecteur)
def nouveau_Detecteur(detecteur: schemas.DetecteurCreate, token_api: str, db: Session = Depends(get_db)):
    """
    Creer un nouveau detecteur dans la base de donnée.</br>
    Pour cerer un detecteur :</br>
        - NameDetecteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/detecteur?token="token",nameDetecteur="DetecteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param detecteur: Json du detecteur à creer
    :param token_api: Token pour acceder à l'API
    :return: json du detecteur créé
    -->
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_detecteur(db, detecteur=detecteur)


"""GET Detecteur"""


@app.get("/detecteur/{id_detecteur}", tags=["Detecteur"], response_model=schemas.Detecteur)
def recuperer_Detecteur(id_detecteur: str, token_api: str, db: Session = Depends(get_db)):
    """
    Creer un nouveau detecteur dans la base de donnée.</br>
    Pour cerer un detecteur :</br>
        - NameDetecteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/detecteur?token="token",nameDetecteur="DetecteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param token_api: str
    :param nameDetecteur: str
    :param latitude: str
    :param longitude: str
    :return: json response.
    -->
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    db_detecteur = crud.get_detecteur(db, id_detecteur=id_detecteur)
    if db_detecteur is None:
        raise HTTPException(status_code=404, detail="Detecteur not found")
    return db_detecteur


@app.get("/detecteurs/", tags=["Detecteur"], response_model=List[schemas.Detecteur])
def recuperer_les_Detecteurs(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Creer un nouveau detecteur dans la base de donnée.</br>
    Pour cerer un detecteur :</br>
        - NameDetecteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/detecteur?token="token",nameDetecteur="DetecteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param token_api: str
    :param nameDetecteur: str
    :param latitude: str
    :param longitude: str
    :return: json response.
    -->
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    detecteurs = crud.get_detecteurs(db, skip=skip, limit=limit)
    return detecteurs


"""PATCH REQUESTS"""


@app.patch("/detecteur/{detecteurs_id}", tags=["Detecteur"], response_model=schemas.Detecteur)
def edit_detecteur(detecteur_id: int, token_api: str, detecteur: schemas.DetecteurUpdate,
                   db: Session = Depends(get_db)):
    """
    PATCH = met a jour uniquement certaines données


    :param detecteur_id: id du detecteur a modifié
    :param token_api: Token pour acceder à l'API
    :param detecteur: JSON des éléments a modifier
    :return: Json du Detecteur modifié
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    detecteur_to_edit = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()
    if detecteur.id_type_detecteur: detecteur_to_edit.id_type_detecteur = detecteur.id_type_detecteur
    if detecteur.latitude_detecteur: detecteur_to_edit.latitude_detecteur = detecteur.latitude_detecteur
    if detecteur.longitude_detecteur: detecteur_to_edit.longitude_detecteur = detecteur.longitude_detecteur
    if detecteur.nom_detecteur: detecteur_to_edit.nom_detecteur = detecteur.nom_detecteur
    db.commit()
    return detecteur_to_edit


"""PUT REQUESTS"""


@app.put("/detecteur/{detecteurs_id}", tags=["Detecteur"], response_model=schemas.Detecteur)
def change_detecteur(detecteur_id: int, detecteur: schemas.DetecteurCreate, token_api: str,
                     db: Session = Depends(get_db)):
    """
    PUT = réécrit
    Réécrir la totalité du detecteur possédant l'id.

    <!--
    :param detecteur_id: id du detecteur (bdd)
    :param detecteur: json du detecteur modifié
    :param token_api: Token pour acceder à l'api
    :return: json du detecteur modifié
    -->
    """

    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    detecteur_to_edit = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()
    detecteur_to_edit.id_type_detecteur = detecteur.id_type_detecteur
    detecteur_to_edit.latitude_detecteur = detecteur.latitude_detecteur
    detecteur_to_edit.longitude_detecteur = detecteur.longitude_detecteur
    detecteur_to_edit.nom_detecteur = detecteur.nom_detecteur
    db.commit()

    return detecteur_to_edit


"""DELETE REQUESTS"""


@app.delete("/detecteur/{detecteurs_id}", tags=["Detecteur"], response_model=schemas.Detecteur)
def delete_detecteur(detecteur_id: int, token_api: str, db: Session = Depends(get_db)):
    """
    DELETE Detecteur by id.

    :param detecteur_id:
    :param token_api:
    :param db:
    :return:
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    detecteur_delete = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()

    if detecteur_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(detecteur_delete)
    db.commit()

    return detecteur_delete


@app.get("/incidents/type/", tags=["type"], response_model=List[schemas.Type_incident])
def recuperer_les_type_incidents(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    type_incidents = crud.get_types_incidents(db, skip=skip, limit=limit)
    return type_incidents


@app.get("/incident/type/name/", tags=["type"], response_model=schemas.Type_incident)
def recuperer_incident_by_name(token_api: str, name_incident: str, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    type_incidents = crud.get_type_incident_by_nom(db, nom_type_incident=name_incident)
    return type_incidents


@app.get("/incident/type/", tags=["type"], response_model=schemas.Type_incident)
def recuperer_incident_by_id(token_api: str, id_incident: int, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    type_incidents = crud.get_type_incident_by_id(db, id_type_incident=id_incident)
    return type_incidents


@app.get("/detecteurs/type/", tags=["type"], response_model=List[schemas.Type_detecteur])
def recuperer_les_type_detecteurs(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    type_detecteurs = crud.get_types_detecteurs(db, skip=skip, limit=limit)
    return type_detecteurs


@app.get("/detecteur/type/name/", tags=["type"], response_model=schemas.Type_detecteur)
def recuperer_detecteur_by_name(token_api: str, name_detecteur: str, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    type_detecteurs = crud.get_type_detecteur_by_nom(db, nom_type_detecteur=name_detecteur)
    return type_detecteurs


@app.get("/detecteur/type/", tags=["type"], response_model=schemas.Type_detecteur)
def recuperer_detecteur_by_id(token_api: str, id_detecteur: int, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    type_detecteurs = crud.get_type_detecteur_by_id(db, id_type_detecteur=id_detecteur)
    return type_detecteurs


@app.post("/detecte/", tags=["Detecte"], response_model=schemas.Detecte)
def create_detecte_event(token_api: str, detecte: schemas.Detecte, db: Session = Depends(get_db)):
    """
    {
      "id_detecteur": 3,
      "intensite_detecte": 25,
      "id_incident": 13,
      "date_detecte": "2022-01-04T10:38:12.197000+00:00"
    }

    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    event = crud.create_detecte_event(db, detecte=detecte)
    return event

@app.get("/detecte/", tags=["Detecte"], response_model=schemas.Detecte)
def get_detecte_event(token_api: str,id_detecteur:int, id_incident:int, db: Session = Depends(get_db)):
    """
    

    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    db_detecteur = crud.get_detecte_event(id_incident,id_detecteur,db)
    if db_detecteur is None:
        raise HTTPException(status_code=404, detail="Event Detecte not found")
    return db_detecteur

@app.get("/detectes/", tags=["Detecte"], response_model=List[schemas.Detecte])
def get_detectes_events(token_api: str,skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    """
    Recupere toutes les liaisons detecte.

    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    db_detecteur = crud.get_detectes_events(db,skip,limit)
    if db_detecteur is None:
        raise HTTPException(status_code=404, detail="Event Detecte not found")
    return db_detecteur

@app.delete("/detecte/", tags=["Detecte"], response_model=schemas.Detecte)
def delete_detecte(id_incident:int, id_detecteur:int, token_api: str, db: Session = Depends(get_db)):
    """
    Supprime une liaison detecte.
    les détécteurs détecent un incident. 

    <!--
    Python : 

        :param id_detecteur: int
        :param id_incident: int
        :param token_api: str
        :return: schema.Detecte
    -->
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    detecte_event_to_delete = db.query(models.Detecte).\
        filter(models.Detecte.id_detecteur == id_detecteur).\
        filter(models.Detecte.id_incident == id_incident).\
        first()

    if detecte_event_to_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(detecte_event_to_delete)
    db.commit()

    return detecte_event_to_delete


"""==============
END CP SIMULATION
=============="""



"""==============
POMPIER
=============="""
@app.post("/pompier", tags=["Pompier"], response_model=schemas.Pompier)
def create_pompier(token_api: str, pompier: schemas.PompierCreate, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_pompier(db, pompier=pompier)


@app.get("/pompier/{id_pompier}", tags=["Pompier"], response_model=schemas.PompierAll)
def get_pompier_id(token_api: str, id_pompier:int, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_pompier_id(db, id_pompier)

@app.get("/pompier/search/", tags=["Pompier"], response_model=List[schemas.PompierAll])
def get_pompier_by_name(token_api: str, nom_pompier: Optional[str] = None, prenom_pompier: Optional[str] = None, matricule_pompier: Optional[int] = None, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_pompier_by_search(db, nom_pompier, prenom_pompier, matricule_pompier)


@app.get("/pompiers/", tags=["Pompier"], response_model=List[schemas.PompierAll])
def get_pompier_all(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_pompier_all(db, skip, limit)


@app.get("/pompiers/{id_caserne}", tags=["Pompier"], response_model=List[schemas.PompierAll])
def get_pompier_id_caserne(token_api: str, id_caserne:int, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_pompier_id_caserne(db, id_caserne)

#post type_pompier
@app.post("/pompier/type", tags=["Pompier","type"], response_model=schemas.Type_pompier)
def create_type_pompier(token_api: str, type_pompier: schemas.Type_pompierCreate, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_type_pompier(db, type_pompier=type_pompier)


@app.get("/pompier/type/{id_type_pompier}", tags=["Pompier","type"], response_model=schemas.Type_pompier)
def get_type_pompier_id(token_api: str, id_type_pompier:int, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_type_pompier_id(db, id_type_pompier)


@app.get("/pompiers/type/", tags=["Pompier","type"], response_model=List[schemas.Type_pompier])
def get_type_pompier_all(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_type_pompier_all(db, skip, limit)


"""==============
CASERNE
=============="""
@app.post("/caserne/", tags=["Caserne"], response_model=schemas.Caserne)
def create_caserne(token_api: str, caserne: schemas.CaserneCreate, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_caserne(db, caserne=caserne)

@app.get("/caserne/{id_caserne}", tags=["Caserne"], response_model=schemas.Caserne)
def get_caserne_id(token_api: str, id_caserne:int, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_caserne_id(db, id_caserne)


@app.get("/casernes/", tags=["Caserne"], response_model=List[schemas.Caserne])
def get_caserne_all(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_caserne_all(db, skip, limit)


"""==============
Vehicule
=============="""
@app.post("/vehicule", tags=["Vehicule"], response_model=schemas.Vehicule)
def create_vehicule(token_api: str, vehicule: schemas.VehiculeCreate, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_vehicule(db, vehicule=vehicule)



@app.get("/vehicule/{id_vehicule}", tags=["Vehicule"], response_model=schemas.VehiculeAll)
def get_vehicule_id(token_api: str, id_vehicule:int, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_vehicule_id(db, id_vehicule)


@app.get("/vehicules/", tags=["Vehicule"], response_model=List[schemas.VehiculeAll])
def get_vehicule_all(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_vehicule_all(db, skip, limit)


@app.get("/vehicules/{id_caserne}", tags=["Vehicule"], response_model=List[schemas.VehiculeAll])
def get_vehicule_id_caserne(token_api: str, id_caserne:int, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_vehicule_id_caserne(db, id_caserne)

#post type_vehicule
@app.post("/vehicule/type", tags=["Vehicule","type"], response_model=schemas.Type_vehicule)
def create_type_vehicule(token_api: str, type_vehicule: schemas.Type_vehiculeCreate, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_type_vehicule(db, type_vehicule=type_vehicule)


@app.get("/vehicule/type/{id_type_vehicule}", tags=["Vehicule","type"], response_model=schemas.Type_vehicule)
def get_type_vehicule_id(token_api: str, id_type_vehicule:int, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_type_vehicule_id(db, id_type_vehicule)


@app.get("/vehicules/type/", tags=["Vehicule","type"], response_model=List[schemas.Type_vehicule])
def get_type_vehicule_all(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.get_type_vehicule_all(db, skip, limit)

