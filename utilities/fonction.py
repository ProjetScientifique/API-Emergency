import re

"""
Regexs verification des données.

-- NOT USED BUT CAN BE. -- 

"""
def isIntensite(element):
    regex = "^[1-9][0-9]?$|^100$"
    if re.match(regex,element):
        return True
    return False

def isLatitude(element):
    regex = "^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)$"
    if re.match(regex,element):
        return True
    return False

def isLongitude(element):
    regex = "^[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$"
    if re.match(regex,element):
        return True
    return False

def isDetecteur(element):
    regex = "^\d$"
    if re.match(regex,element):
        return True
    return False