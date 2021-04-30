from num2words import num2words
from datetime import datetime

months = {
    1 : "enero",
    2 : "febrero",
    3 : "marzo",
    4 : "abril",
    5 : "mayo",
    6 : "junio",
    7 : "julio",
    8 : "agosto",
    9 : "septiembre",
    10 : "octubre",
    11 : "noviembre",
    12 : "diciembre",
}

def getSpanishStringDate():
    date = datetime.today()
    day = num2words(date.day, lang="es")
    month = date.month 
    year = num2words(date.year, lang="es")

    dateString = f"{day} de {months[month]} de {year}"
    return dateString