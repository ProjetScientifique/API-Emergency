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

class IncidentBase(BaseModel):
    id_type_incident: int
    latitude_incident: float
    longitude_incident: float
    intensite_incident: float
    date_incident: datetime.datetime


class IncidentUpdate(BaseModel):
    id_type_incident: Optional[int]
    latitude_incident: Optional[float]
    longitude_incident: Optional[float]
    intensite_incident: Optional[float]
    date_incident: Optional[datetime.datetime]

class IncidentCreate(IncidentBase):
    pass

class Incident(IncidentBase):
    id_incident: int
    type_incident : Type_incident
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
    id_type_detecteur: int
    latitude_detecteur: float
    longitude_detecteur: float
    nom_detecteur: str


class DetecteurUpdate(BaseModel):
    id_type_detecteur: Optional[int]
    latitude_detecteur: Optional[float]
    longitude_detecteur: Optional[float]
    nom_detecteur: Optional[str]


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




"""
Detecte.
"""

class Detecte(BaseModel):
    id_incident: int
    id_detecteur: int
    date_detecte: datetime.datetime
    intensite_detecte: float
    class Config:
        orm_mode = True
