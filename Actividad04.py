import requests
from colorama import *
def requestActor():
    print(Fore.BLUE+"Fecha de Nacimiento y Signo del Zodíaco del actor de Dragon Ball:")
    url = "https://moviesminidatabase.p.rapidapi.com/actor/id/nm0154226/"

    headers = {
        "X-RapidAPI-Key": "20f84019f0mshee865c33ed4221dp1c2e20jsnfc95cc0881a0",
        "X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'birth_date' in data['results']:
        title_value = data['results']['birth_date']
        description_value = data['results']['star_sign']
        print(Fore.LIGHTGREEN_EX+"Fecha de Nacimiento del actor: "+title_value+"\nSigno del zodíaco: "+description_value)
    else:
        print(Fore.LIGHTGREEN_EX+"No se ha podido acceder a la informacion")