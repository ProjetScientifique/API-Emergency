from sqlalchemy.orm import Session
from . import models, schemas


def get_incident(db: Session, incident_id: int):
    return db.query(models.Incident). \
        filter(models.Incident.id_incident == incident_id). \
        first()

def get_incidents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Incident).offset(skip).limit(limit).all()


def create_incidents(db: Session, incident: schemas.IncidentCreate):
    db_incident = models.Incident(id_type_incident=incident.id_type_incident,
                                  latitude_incident=incident.latitude_incident,
                                  longitude_incident=incident.longitude_incident,
                                  intensite_incident=incident.intensite_incident,
                                  date_incident=incident.date_incident)
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


def get_detecteur(db: Session, id_detecteur: int):
    return db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == id_detecteur).first()


def get_detecteurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detecteur).offset(skip).limit(limit).all()


def create_detecteur(db: Session, detecteur: schemas.DetecteurCreate):
    db_detecteur = models.Detecteur(id_type_detecteur=detecteur.id_type_detecteur,
                                    latitude_detecteur=detecteur.latitude_detecteur,
                                    longitude_detecteur=detecteur.longitude_detecteur,
                                    nom_detecteur=detecteur.nom_detecteur)
    db.add(db_detecteur)
    db.commit()
    db.refresh(db_detecteur)
    return db_detecteur


def get_type_incident_by_id(db: Session, id_type_incident: int):
    return db.query(models.Type_incident).filter(models.Type_incident.id_type_incident == id_type_incident).first()


def get_type_incident_by_nom(db: Session, nom_type_incident: str):
    return db.query(models.Type_incident).filter(models.Type_incident.nom_type_incident == nom_type_incident).first()


def get_types_incidents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Type_incident).offset(skip).limit(limit).all()


def get_type_detecteur_by_id(db: Session, id_type_detecteur: int):
    return db.query(models.Type_detecteur).filter(models.Type_detecteur.id_type_detecteur == id_type_detecteur).first()


def get_type_detecteur_by_nom(db: Session, nom_type_detecteur: str):
    return db.query(models.Type_detecteur).filter(
        models.Type_detecteur.nom_type_detecteur == nom_type_detecteur).first()


def get_types_detecteurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Type_detecteur).offset(skip).limit(limit).all()

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


def get_detecte_event(id_incident:int , id_detecteur:int ,db: Session):
    return db.query(models.Detecte).\
        filter(models.Detecte.id_detecteur == id_detecteur).\
        filter(models.Detecte.id_incident == id_incident).\
        first()

def get_detectes_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detecte).offset(skip).limit(limit).all()