import json

import requests
from colorama import init, Fore


def cantSeries():
    init(autoreset=True)
    search = "Dragon%20Ball"
    url = "https://moviesminidatabase.p.rapidapi.com/series/idbyTitle/" + search + "/"
    headers = {
        "X-RapidAPI-Key": "cef161a3abmshf4d3a8d8d818ad6p1f0597jsn7eaf4822b2a0",
        "X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
    }
    print(Fore.BLUE + "Número de Series de Dragon Ball:\n\n")
    response = requests.get(url, headers=headers)
    data = response.json()
    if data['results']:
        quantity = 1
        for d in data['results']:
            quantity += 1
        print(Fore.LIGHTGREEN_EX + "La cantidad de series de Dragon Ball es: " + str(quantity))
    else:
        print("No se han encontrado series de Dragon Ball")
