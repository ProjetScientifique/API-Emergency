from typing import List, Optional
from pydantic import BaseModel
import datetime

"""
.___              .__    .___             __   
|   | ____   ____ |__| __| _/____   _____/  |_ 
|   |/    \_/ ___\|  |/ __ |/ __ \ /    \   __\
|   |   |  \  \___|  / /_/ \  ___/|   |  \  |  
|___|___|  /\___  >__\____ |\___  >___|  /__|  
         \/     \/        \/    \/     \/      
"""


class Type_incident(BaseModel):
    id_type_incident: int
    nom_type_incident: str

    class Config:
        orm_mode = True


class Type_status_incident(BaseModel):
    id_type_status_incident: int
    nom_type_status_incident: str

    class Config:
        orm_mode = True

class IncidentBase(BaseModel):
    id_type_incident: int
    latitude_incident: float
    longitude_incident: float
    intensite_incident: float
    date_incident: datetime.datetime
    id_type_status_incident: int

    class Config:
        orm_mode = True

class IncidentUpdate(BaseModel):
    id_type_incident: Optional[int]
    latitude_incident: Optional[float]
    longitude_incident: Optional[float]
    intensite_incident: Optional[float]
    date_incident: Optional[datetime.datetime]
    id_type_status_incident: Optional[int]

class IncidentCreate(IncidentBase):
    pass

class Incident(IncidentBase):
    id_incident: int
    
    class Config:
        orm_mode = True

class IncidentAll(Incident):
    type_incident : Type_incident
    type_status_incident : Type_status_incident

    class Config:
        orm_mode = True


"""
________          __                 __                       
\______ \   _____/  |_  ____   _____/  |_  ____  __ _________ 
 |    |  \_/ __ \   __\/ __ \_/ ___\   __\/ __ \|  |  \_  __ \
 |    `   \  ___/|  | \  ___/\  \___|  | \  ___/|  |  /|  | \/
/_______  /\___  >__|  \___  >\___  >__|  \___  >____/ |__|   
        \/     \/          \/     \/          \/              
"""


class DetecteurBase(BaseModel):
    id_detecteur: Optional[int]
    id_type_detecteur: int
    latitude_detecteur: float
    longitude_detecteur: float


class DetecteurUpdate(BaseModel):
    id_type_detecteur: Optional[int]
    latitude_detecteur: Optional[float]
    longitude_detecteur: Optional[float]


class DetecteurCreate(DetecteurBase):
    pass


class Detecteur(DetecteurBase):
    id_detecteur: int

    class Config:
        orm_mode = True


class Type_detecteur(BaseModel):
    id_type_detecteur: int
    nom_type_detecteur: str

    class Config:
        orm_mode = True

class Type_detecteurCreate(Type_detecteur):
    pass



"""
JE sais pas
"""

class Detecte(BaseModel):
    id_incident: int
    id_detecteur: int
    date_detecte: datetime.datetime
    intensite_detecte: float
    class Config:
        orm_mode = True

class Intervient(BaseModel):
    id_pompier: int
    id_vehicule: int 
    id_incident: int
    date_intervient: datetime.datetime
    class Config:
        orm_mode = True

"""
_________                                           
\_   ___ \_____    ______ ___________  ____   ____  
/    \  \/\__  \  /  ___// __ \_  __ \/    \_/ __ \ 
\     \____/ __ \_\___ \\  ___/|  | \/   |  \  ___/ 
 \______  (____  /____  >\___  >__|  |___|  /\___  >
        \/     \/     \/     \/           \/     \/ 

"""

class CaserneBase(BaseModel):
    nom_caserne: str
    latitude_caserne: float
    longitude_caserne: float
    class Config:
        orm_mode = True

class CaserneUpdate(BaseModel):
   
    nom_caserne: Optional[str]
    latitude_caserne: Optional[float]
    longitude_caserne: Optional[float]

    class Config:
        orm_mode = True

class CaserneCreate(CaserneBase):
    pass

class Caserne(CaserneBase):
    id_caserne: int
    class Config:
        orm_mode = True


"""
__________                     .__              
\______   \____   _____ ______ |__| ___________ 
 |     ___/  _ \ /     \\____ \|  |/ __ \_  __ \
 |    |  (  <_> )  Y Y  \  |_> >  \  ___/|  | \/
 |____|   \____/|__|_|  /   __/|__|\___  >__|   
                      \/|__|           \/       

"""

class Type_pompierBase(BaseModel):
    nom_type_pompier: str
    efficacite_type_pompier: int
    

class Type_pompierCreate(Type_pompierBase):
    pass

class Type_pompier(Type_pompierBase):
    id_type_pompier: int
    class Config:
        orm_mode = True


class PompierBase(BaseModel):
    id_caserne: int
    id_type_pompier: int
    nom_pompier: str
    prenom_pompier: str
    date_naissance_pompier: datetime.date
    nombre_intervention_jour_maximum_pompier: int
    disponibilite_pompier: bool

    class Config:
        orm_mode = True

class PompierCreate(PompierBase):
   pass

class PompierUpdate(BaseModel):
    id_caserne: Optional[int]
    id_type_pompier: Optional[int]
    #nom_pompier: Optional[str]
    #prenom_pompier: Optional[str]
    #date_naissance_pompier: Optional[datetime.datetime]
    nombre_intervention_jour_maximum_pompier: Optional[int]
    disponibilite_pompier: Optional[bool]

    class Config:
        orm_mode = True

class Pompier(PompierBase):
    id_pompier: int

    class Config:
        orm_mode= True
    
    

class PompierAll(Pompier):
    type_pompier: Type_pompier
    caserne: CaserneBase

    class Config:
        orm_mode = True


"""
____   ____     .__    .__             .__          
\   \ /   /____ |  |__ |__| ____  __ __|  |   ____  
 \   Y   // __ \|  |  \|  |/ ___\|  |  \  | _/ __ \ 
  \     /\  ___/|   Y  \  \  \___|  |  /  |_\  ___/ 
   \___/  \___  >___|  /__|\___  >____/|____/\___  >
              \/     \/        \/                \/ 
"""



class Type_vehiculeCreate(BaseModel):
    nom_type_vehicule: str
    capacite_type_vehicule: int
    puissance_intervention_type_vehicule: int
    class Config:
        orm_mode = True

#type
class Type_vehicule(Type_vehiculeCreate):
    id_type_vehicule: int
    
    class Config:
        orm_mode = True

#disponibilite
class Type_disponibilite_vehicule(BaseModel):
    id_type_disponibilite_vehicule: int
    nom_type_disponibilite_vehicule: str

    class Config:
        orm_mode = True


class VehiculeBase(BaseModel):
    id_caserne: int
    id_type_vehicule: int
    id_type_disponibilite_vehicule: int
    annee_vehicule: int
    nombre_intervention_maximum_vehicule: int
    latitude_vehicule: float
    longitude_vehicule: float

    class Config:
        orm_mode = True


class VehiculeUpdate(BaseModel):
    id_caserne: Optional[int]
    id_type_disponibilite_vehicule: Optional[int]
    nombre_intervention_maximum_vehicule: Optional[int]
    latitude_vehicule: Optional[float]
    longitude_vehicule: Optional[float]

class VehiculeCreate(VehiculeBase):
    pass

class Vehicule(VehiculeBase):
    id_vehicule: int

    class Config:
        orm_mode = True

class VehiculeAll(Vehicule):
    type_vehicule: Type_vehicule
    caserne: CaserneBase
    type_disponibilite_vehicule: Type_disponibilite_vehicule

    class Config:
        orm_mode = True