import requests
from colorama import *


def peliculaNominada():
    print(Fore.BLUE+"Película nominada a los oscar, nominaciones y ganados: ")
    url = "https://moviesminidatabase.p.rapidapi.com/movie/id/tt0084516/awards/"
    headers = {
        "X-RapidAPI-Key": "20f84019f0mshee865c33ed4221dp1c2e20jsnfc95cc0881a0",
        "X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)

    data = response.json()
    if 'award' in data['results'][0]:
        nominado = data['results'][0]['movie']['title']
        nominadoA = data['results'][0]['award']
        premio = data['results'][1]['award']
        premio2 = data['results'][2]['award']
        print(Fore.LIGHTGREEN_EX + "Película nominada: " + nominado)
        print(Fore.LIGHTGREEN_EX + "Premios nominados: " + nominadoA)
        print(Fore.LIGHTGREEN_EX + "Premios ganados: " + premio + ", " + premio2)
    else:
        print(Fore.LIGHTGREEN_EX + "No se encuentran películas de ese año")
