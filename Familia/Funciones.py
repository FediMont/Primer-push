import time
from datetime import date,datetime

def age_calc(ddmmaaaa):
    a = ddmmaaaa.strftime("%d/%m/%Y") #Esto reordena en dd/mm/aaaa
    dd = int(a.split('/')[0]) #Esto extrae los valores separados por '/'
    mm = int(a.split('/')[1]) #Para obtener cada variable por separado
    aa = int(a.split('/')[2]) #Y asi aplicarle age_calc(dd_padre,mm_padre,aa_padre)

    DD = int(date.today().day)
    MM = int(date.today().month)
    AA = int(date.today().year)
    
    if MM == mm and DD == dd:
        edad = AA-aa
        return edad
    elif MM == mm and DD > dd:
        edad = AA-aa
        return edad
    elif MM == mm and DD < dd:
        edad = (AA-aa) - 1
        return edad    
    elif MM > mm:
        edad = AA-aa
        return edad    
    elif MM > mm:
        edad = AA-aa
        return edad
    elif MM < mm:
        edad = (AA-aa) - 1
        return edad

class Familiar:
    especie = 'persona'

    def __init__(self, nombre, apellido, nacimiento, vinculo):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento.strftime("%d/%m/%Y")
        self.edad = age_calc(nacimiento)
        self.vinculo = vinculo

class Mascota:
    especie = 'animal'

    def __init__(self, nombre, adopcion):
        self.nombre = nombre
        self.adopcion = adopcion.strftime("%d/%m/%Y")