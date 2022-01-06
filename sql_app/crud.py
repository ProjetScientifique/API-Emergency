from sqlalchemy.orm import Session
from sqlalchemy import func 
from . import models, schemas
from fastapi import HTTPException


"""
.___              .__    .___             __   
|   | ____   ____ |__| __| _/____   _____/  |_ 
|   |/    \_/ ___\|  |/ __ |/ __ \ /    \   __\
|   |   |  \  \___|  / /_/ \  ___/|   |  \  |  
|___|___|  /\___  >__\____ |\___  >___|  /__|  
         \/     \/        \/    \/     \/      
"""
# get 1 incident
def get_incident(db: Session, incident_id: int):
    return db.query(models.Incident). \
        filter(models.Incident.id_incident == incident_id). \
        first()
# get all incidents
def get_incidents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Incident).offset(skip).limit(limit).all()

# create un incident
def create_incidents(db: Session, incident: schemas.IncidentCreate):
    db_incident = models.Incident(id_type_incident=incident.id_type_incident,
                                  latitude_incident=incident.latitude_incident,
                                  longitude_incident=incident.longitude_incident,
                                  intensite_incident=incident.intensite_incident,
                                  date_incident=incident.date_incident,
                                  id_type_status_incident=incident.id_type_status_incident)
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

# patch un incident
def patch_incident(db: Session, incident: schemas.IncidentUpdate, incident_id: int):
    incident_to_edit = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()
    if incident.id_type_incident: incident_to_edit.id_type_incident = incident.id_type_incident
    if incident.latitude_incident: incident_to_edit.latitude_incident = incident.latitude_incident
    if incident.longitude_incident: incident_to_edit.longitude_incident = incident.longitude_incident
    if incident.intensite_incident: incident_to_edit.intensite_incident = incident.intensite_incident
    if incident.date_incident: incident_to_edit.date_incident = incident.date_incident
    if incident.id_type_status_incident: incident_to_edit.id_type_status_incident = incident.id_type_status_incident

    db.commit()
    return incident_to_edit

# put un incident
def put_incident(db: Session, incident: schemas.IncidentUpdate, incident_id: int):
    incident_to_edit = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()
    incident_to_edit.latitude_incident = incident.latitude_incident
    incident_to_edit.longitude_incident = incident.longitude_incident
    incident_to_edit.intensite_incident = incident.intensite_incident
    incident_to_edit.date_incident = incident.date_incident
    incident_to_edit.id_type_status_incident = incident.id_type_status_incident

    db.commit()
    return incident_to_edit

# delete un incident
def delete_incident(db: Session, incident_id: int):
    incident_delete = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()

    if incident_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(incident_delete)
    db.commit()

    return incident_delete


"""
________          __                 __          
\______ \   _____/  |_  ____   _____/  |_  ____  
 |    |  \_/ __ \   __\/ __ \_/ ___\   __\/ __ \ 
 |    `   \  ___/|  | \  ___/\  \___|  | \  ___/ 
/_______  /\___  >__|  \___  >\___  >__|  \___  >
        \/     \/          \/     \/          \/       
"""

# get un detecteur
def get_detecteur(db: Session, id_detecteur: int):
    return db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == id_detecteur).first()

# get tous les detecteurs
def get_detecteurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detecteur).offset(skip).limit(limit).all()

# create un detecteur
def create_detecteur(db: Session, detecteur: schemas.DetecteurCreate):
    db_detecteur = models.Detecteur(id_type_detecteur=detecteur.id_type_detecteur,
                                    latitude_detecteur=detecteur.latitude_detecteur,
                                    longitude_detecteur=detecteur.longitude_detecteur)
    db.add(db_detecteur)
    db.commit()
    db.refresh(db_detecteur)
    return db_detecteur

# patch un detecteur
def patch_detecteur(db: Session, detecteur: schemas.DetecteurUpdate, detecteur_id: int):
    
    detecteur_to_patch = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()
    
    if detecteur.id_type_detecteur: detecteur_to_patch.id_type_detecteur = detecteur.id_type_detecteur
    if detecteur.latitude_detecteur: detecteur_to_patch.latitude_detecteur = detecteur.latitude_detecteur
    if detecteur.longitude_detecteur: detecteur_to_patch.longitude_detecteur = detecteur.longitude_detecteur
    
    db.commit()
    return detecteur_to_patch

# put un detecteur
def put_detecteur(db: Session, detecteur: schemas.DetecteurUpdate, detecteur_id: int):
    
    detecteur_to_put = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()
    detecteur_to_put.id_type_detecteur = detecteur.id_type_detecteur
    detecteur_to_put.latitude_detecteur = detecteur.latitude_detecteur
    detecteur_to_put.longitude_detecteur = detecteur.longitude_detecteur

    db.commit()
    return detecteur_to_put

# delete un detecteur
def delete_detecteur(db: Session, detecteur_id: int):
    detecteur_to_delete = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()

    if detecteur_to_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(detecteur_to_delete)
    db.commit()
    return detecteur_to_delete

# get type incident par l'id
def get_type_incident_by_id(db: Session, id_type_incident: int):
    return db.query(models.Type_incident).filter(models.Type_incident.id_type_incident == id_type_incident).first()

# get type incident par le nom
def get_type_incident_by_nom(db: Session, nom_type_incident: str):
    return db.query(models.Type_incident).filter(models.Type_incident.nom_type_incident == nom_type_incident).first()

# get tous les types incendies
def get_types_incidents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Type_incident).offset(skip).limit(limit).all()

# get type detecteur par l'id
def get_type_detecteur_by_id(db: Session, id_type_detecteur: int):
    return db.query(models.Type_detecteur).filter(models.Type_detecteur.id_type_detecteur == id_type_detecteur).first()

# get type detecteur par le nom
def get_type_detecteur_by_nom(db: Session, nom_type_detecteur: str):
    return db.query(models.Type_detecteur).filter(
        models.Type_detecteur.nom_type_detecteur == nom_type_detecteur).first()

# create type detecteur 
def create_type_detecteur(db: Session, type_detecteur: schemas.Type_detecteurCreate):
    db_type_detecteur = models.Type_detecteur(
        nom_type_detecteur = type_detecteur.nom_type_detecteur,
    )
    db.add(db_type_detecteur)
    db.commit()
    db.refresh(db_type_detecteur)
    return db_type_detecteur

# get tous les types de detecteurs
def get_types_detecteurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Type_detecteur).offset(skip).limit(limit).all()

# create detection
def create_detecte_event(db: Session, detecte: schemas.Detecte):
    db_detect = models.Detecte(id_incident=detecte.id_incident,
                               id_detecteur=detecte.id_detecteur,
                               date_detecte=detecte.date_detecte,
                               intensite_detecte=detecte.intensite_detecte
                               )
    db.add(db_detect)
    db.commit()
    db.refresh(db_detect)
    return db_detect

# get une detection par l'id incident et detecteur
def get_detecte_event(id_incident:int , id_detecteur:int ,db: Session):
    return db.query(models.Detecte).\
        filter(models.Detecte.id_detecteur == id_detecteur).\
        filter(models.Detecte.id_incident == id_incident).\
        first()

# get toutes les detections
def get_detectes_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detecte).offset(skip).limit(limit).all()



"""Pompier"""

# create un pompier
def create_pompier(db: Session, pompier: schemas.PompierCreate):
    db_pompier = models.Pompier(
        id_caserne = pompier.id_caserne,
        id_type_pompier = pompier.id_type_pompier,
        nom_pompier = pompier.nom_pompier,
        prenom_pompier = pompier.prenom_pompier,
        date_naissance_pompier = pompier.date_naissance_pompier,
        nombre_intervention_jour_maximum_pompier = pompier.nombre_intervention_jour_maximum_pompier,
        disponibilite_pompier= pompier.disponibilite_pompier
    )
    db.add(db_pompier)
    db.commit()
    db.refresh(db_pompier)
    return db_pompier

# get un pompier par l'id
def get_pompier_id(db: Session, pompier_id: int):
    return db.query(models.Pompier). \
        filter(models.Pompier.id_pompier == pompier_id). \
        first()

# récupérer un pompier par le nom et/ou prénom et/ou matricule (id)
def get_pompier_by_search(db: Session, pompier_nom: str=False,pompier_prenom: str=False, id_pompier: int=False):
    pompier_nom = f"%{pompier_nom}%".lower()
    pompier_prenom = f"%{pompier_prenom}%".lower()
    q = db.query(models.Pompier)
    if pompier_nom: q.filter(func.lower(models.Pompier.nom_pompier).like(pompier_nom))
    if pompier_prenom: q.filter(func.lower(models.Pompier.nom_pompier).like(pompier_prenom))
    if id_pompier: q.filter(models.Pompier.id_pompier == id_pompier)
    return q.all()

# get les pompier par caserne
def get_pompier_id_caserne(db: Session, caserne_id: int):
    return db.query(models.Pompier). \
        filter(models.Pompier.id_caserne == caserne_id). \
        all()

# get tous les pompiers
def get_pompier_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pompier).offset(skip).limit(limit).all()

# create un type de pompier
def create_type_pompier(db: Session, type_pompier: schemas.Type_pompierCreate):
    db_type_pompier = models.Type_pompier(
        nom_type_pompier = type_pompier.nom_type_pompier,
        efficacite_type_pompier = type_pompier.efficacite_type_pompier
    )
    db.add(db_type_pompier)
    db.commit()
    db.refresh(db_type_pompier)
    return db_type_pompier

# get un type de pompier par l'id
def get_type_pompier_id(db: Session, id_type_pompier:int):
    return db.query(models.Type_pompier). \
        filter(models.Type_pompier.id_type_pompier == id_type_pompier). \
        first()

# get tous les types de pompiers
def get_type_pompier_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Type_pompier).offset(skip).limit(limit).all()

"""caserne"""
# create caserne
def create_caserne(db: Session, caserne: schemas.CaserneCreate):
    db_caserne = models.Caserne(
        nom_caserne = caserne.nom_caserne,
        latitude_caserne = caserne.latitude_caserne,
        longitude_caserne = caserne.longitude_caserne
    )
    db.add(db_caserne)
    db.commit()
    db.refresh(db_caserne)
    return db_caserne

# get une caserne par l'id
def get_caserne_id(db: Session, id_caserne:int):
    return db.query(models.Caserne). \
        filter(models.Caserne.id_caserne == id_caserne). \
        first()

# get toutes les casernes
def get_caserne_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Caserne).offset(skip).limit(limit).all()

"""vehicule"""
# create un vehicule
def create_vehicule(db: Session, vehicule: schemas.VehiculeCreate):
    db_vehicule = models.Vehicule(
        id_caserne = vehicule.id_caserne,
        id_type_vehicule = vehicule.id_type_vehicule,
        id_type_disponibilite_vehicule = vehicule.id_type_disponibilite_vehicule,
        annee_vehicule = vehicule.annee_vehicule,
        nombre_intervention_maximum_vehicule = vehicule.nombre_intervention_maximum_vehicule,
        latitude_vehicule = vehicule.latitude_vehicule,
        longitude_vehicule = vehicule.longitude_vehicule
    )
    db.add(db_vehicule)
    db.commit()
    db.refresh(db_vehicule)
    return db_vehicule

# get un véhicule par l'id
def get_vehicule_id(db: Session, vehicule_id: int):
    return db.query(models.Vehicule). \
        filter(models.Vehicule.id_vehicule == vehicule_id). \
        first()

"""
# PEU SERVIR 
# recherche par : 
# annee
# capacite ?
# 
# TODO
def get_vehicule_by_search(db: Session, vehicule_nom: str=False,vehicule_prenom: str=False, id_vehicule: int=False):
    vehicule_nom = f"%{vehicule_nom}%".lower()
    vehicule_prenom = f"%{vehicule_prenom}%".lower()
    q = db.query(models.Vehicule)
    if vehicule_nom: q.filter(func.lower(models.Vehicule.nom_vehicule).like(vehicule_nom))
    if vehicule_prenom: q.filter(func.lower(models.Vehicule.nom_vehicule).like(vehicule_prenom))
    if id_vehicule: q.filter(models.Vehicule.id_vehicule == id_vehicule)
    return q.all()
"""
# get les véhicules affecté à une caserne
def get_vehicule_id_caserne(db: Session, caserne_id: int):
    return db.query(models.Vehicule). \
        filter(models.Vehicule.id_caserne == caserne_id). \
        all()

# get tous les véhicules
def get_vehicule_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vehicule).offset(skip).limit(limit).all()

# create un type de vehicule
def create_type_vehicule(db: Session, type_vehicule: schemas.Type_vehiculeCreate):
    db_type_vehicule = models.Type_vehicule(
        nom_type_vehicule = type_vehicule.nom_type_vehicule,
        capacite_type_vehicule = type_vehicule.capacite_type_vehicule,
        puissance_intervention_type_vehicule = type_vehicule.puissance_intervention_type_vehicule
    )
    db.add(db_type_vehicule)
    db.commit()
    db.refresh(db_type_vehicule)
    return db_type_vehicule

# get type vehicule par l'id
def get_type_vehicule_id(db: Session, id_type_vehicule:int):
    return db.query(models.Type_vehicule). \
        filter(models.Type_vehicule.id_type_vehicule == id_type_vehicule). \
        first()

# get tous les type de vehicules
def get_type_vehicule_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Type_vehicule).offset(skip).limit(limit).all()
