from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Numeric
from sqlalchemy.orm import relationship

from .database import Base

"""
.___              .__    .___             __   
|   | ____   ____ |__| __| _/____   _____/  |_ 
|   |/    \_/ ___\|  |/ __ |/ __ \ /    \   __\
|   |   |  \  \___|  / /_/ \  ___/|   |  \  |  
|___|___|  /\___  >__\____ |\___  >___|  /__|  
         \/     \/        \/    \/     \/      
"""

class Type_incident(Base):
    __tablename__ = "type_incident"
    id_type_incident = Column(Integer, primary_key=True)
    nom_type_incident = Column(String)

    incidents = relationship("Incident", back_populates="type_incident")

class Type_status_incident(Base):
    __tablename__ = "type_status_incident"
    id_type_status_incident = Column(Integer, primary_key=True)
    nom_type_status_incident = Column(String)

    incidents = relationship("Incident", back_populates="type_status_incident")


class Incident(Base):
    __tablename__ = "incident"
    id_incident = Column(Integer, primary_key=True)
    id_type_incident = Column(Integer, ForeignKey('type_incident.id_type_incident'))
    id_type_status_incident = Column(Integer, ForeignKey('type_status_incident.id_type_status_incident'))
    date_incident = Column(TIMESTAMP)
    latitude_incident = Column(Numeric(precision=9, scale=7))
    longitude_incident = Column(Numeric(precision=10, scale=7))
    intensite_incident = Column(Numeric(precision=4, scale=2))

    type_incident = relationship("Type_incident", back_populates="incidents")
    type_status_incident = relationship("Type_status_incident", back_populates="incidents")
    detecte = relationship("Detecte", back_populates="incident")
    intervient = relationship("Intervient", back_populates="incident")


"""
________          __                 __                       
\______ \   _____/  |_  ____   _____/  |_  ____  __ _________ 
 |    |  \_/ __ \   __\/ __ \_/ ___\   __\/ __ \|  |  \_  __ \
 |    `   \  ___/|  | \  ___/\  \___|  | \  ___/|  |  /|  | \/
/_______  /\___  >__|  \___  >\___  >__|  \___  >____/ |__|   
        \/     \/          \/     \/          \/              
"""


class Type_detecteur(Base):
    __tablename__ = "type_detecteur"
    id_type_detecteur = Column(Integer, primary_key=True)
    nom_type_detecteur = Column(String)

    detecteur = relationship("Detecteur", back_populates="type")


class Detecteur(Base):
    __tablename__ = "detecteur"
    id_detecteur = Column(Integer, primary_key=True)
    id_type_detecteur = Column(Integer, ForeignKey('type_detecteur.id_type_detecteur'))
    nom_detecteur = Column(String)
    latitude_detecteur = Column(Numeric(precision=9, scale=7))
    longitude_detecteur = Column(Numeric(precision=10, scale=7))

    type = relationship("Type_detecteur", back_populates="detecteur")
    detecte = relationship("Detecte", back_populates="detecteur")

"""
JE SAIS PAS 
"""

class Detecte(Base):
    __tablename__ = "detecte"
    id_incident = Column(Integer, ForeignKey('incident.id_incident'), primary_key=True)
    id_detecteur = Column(Integer, ForeignKey('detecteur.id_detecteur'), primary_key=True)
    date_detecte = Column(TIMESTAMP)
    intensite_detecte = Column(Numeric(precision=4, scale=2))

    incident = relationship("Incident", back_populates="detecte")
    detecteur = relationship("Detecteur", back_populates="detecte")

class Intervient(Base):
    __tablename__ = "intervient"
    id_pompier = Column(Integer, ForeignKey('pompier.id_pompier'), primary_key=True)
    id_vehicule = Column(Integer, ForeignKey('vehicule.id_vehicule'), primary_key=True)
    id_incident = Column(Integer, ForeignKey('incident.id_incident'), primary_key=True)
    date_intervient = Column(TIMESTAMP)

    incident = relationship("Incident", back_populates="intervient")
    vehicule = relationship("Vehicule", back_populates="intervient")
    pompier = relationship("Pompier", back_populates="intervient")

"""
__________                     .__              
\______   \____   _____ ______ |__| ___________ 
 |     ___/  _ \ /     \\____ \|  |/ __ \_  __ \
 |    |  (  <_> )  Y Y  \  |_> >  \  ___/|  | \/
 |____|   \____/|__|_|  /   __/|__|\___  >__|   
                      \/|__|           \/       

"""


class Type_pompier(Base):
    __tablename__ = "type_pompier"
    id_type_pompier = Column(Integer, primary_key=True)
    nom_type_pompier = Column(String)
    efficacite_type_pompier = Column(Integer)

    pompier = relationship("Pompier", back_populates="type_pompier")


class Pompier(Base):
    __tablename__ = "pompier"
    id_pompier = Column(Integer, primary_key=True)
    id_caserne = Column(Integer, ForeignKey('caserne.id_caserne'))
    id_type_pompier = Column(Integer, ForeignKey('type_pompier.id_type_pompier'))
    nom_pompier = Column(String)
    prenom_pompier = Column(String)
    date_naissance_pompier = Column(TIMESTAMP)
    nombre_intervention_jour_maximum_pompier = Column(Integer)
    disponibilite_pompier = Column(Boolean)

    type_pompier = relationship("Type_pompier", back_populates="pompier")
    intervient = relationship("Intervient", back_populates="pompier")
    caserne = relationship("Caserne", back_populates="pompier")
    
    
"""
_________                                           
\_   ___ \_____    ______ ___________  ____   ____  
/    \  \/\__  \  /  ___// __ \_  __ \/    \_/ __ \ 
\     \____/ __ \_\___ \\  ___/|  | \/   |  \  ___/ 
 \______  (____  /____  >\___  >__|  |___|  /\___  >
        \/     \/     \/     \/           \/     \/ 

"""

class Caserne(Base):
    __tablename__ = "caserne"
    id_caserne = Column(Integer, primary_key=True)
    nom_caserne = Column(String)
    latitude_caserne = Column(Numeric(precision=9, scale=7))
    longitude_caserne = Column(Numeric(precision=10, scale=7))

    vehicule = relationship("Vehicule", back_populates="caserne")
    pompier = relationship("Pompier", back_populates="caserne")

"""
____   ____     .__    .__             .__          
\   \ /   /____ |  |__ |__| ____  __ __|  |   ____  
 \   Y   // __ \|  |  \|  |/ ___\|  |  \  | _/ __ \ 
  \     /\  ___/|   Y  \  \  \___|  |  /  |_\  ___/ 
   \___/  \___  >___|  /__|\___  >____/|____/\___  >
              \/     \/        \/                \/ 
"""


class Type_vehicule(Base):
    __tablename__ = "type_vehicule"
    id_type_vehicule = Column(Integer, primary_key=True)
    nom_type_vehicule = Column(String)
    capacite_type_vehicule = Column(Integer)
    puissance_intervention_type_vehicule = Column(Integer)

    vehicule = relationship("Vehicule", back_populates="type_vehicule")


class Type_disponibilite_vehicule(Base):
    __tablename__ = "type_disponibilite_vehicule"
    id_type_disponibilite_vehicule = Column(Integer, primary_key=True)
    nom_type_disponibilite_vehicule = Column(String)

    vehicule = relationship("Vehicule", back_populates="type_disponibilie_vehicule")


class Vehicule(Base):
    __tablename__ = "vehicule"
    id_vehicule = Column(Integer, primary_key=True)
    id_caserne = Column(Integer, ForeignKey('caserne.id_caserne'))
    id_type_vehicule = Column(Integer, ForeignKey('type_vehicule.id_type_vehicule'))
    id_type_disponibilie_vehicule = Column(Integer, ForeignKey('type_disponibilite_vehicule.id_type_disponibilite_vehicule'))
    annee_vehicule = Column(Integer)
    nombre_intervention_maximum_vehicule = Column(Integer)
    latitude_vehicule = Column(Numeric(precision=9, scale=7))
    longitude_vehicule = Column(Numeric(precision=10, scale=7))


    caserne = relationship("Caserne", back_populates="vehicule")
    type_vehicule = relationship("Type_vehicule", back_populates="vehicule")
    type_disponibilie_vehicule = relationship("Type_disponibilite_vehicule", back_populates="vehicule")
    intervient = relationship("Intervient", back_populates="vehicule")

    

    
    






