import requests
from colorama import *
def tituloSerie():
    print(Fore.BLUE+"Título y argumento de el episodio 1 de la temporada 3 de Dragon Ball: ")
    url = "https://moviesminidatabase.p.rapidapi.com/series/id/tt0280249/season/3/episode/1/"

    headers = {
        "X-RapidAPI-Key": "20f84019f0mshee865c33ed4221dp1c2e20jsnfc95cc0881a0",
        "X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'title' in data['results']:
        title_value = data['results']['title']
        description_value = data['results']['description']
        print(Fore.LIGHTGREEN_EX + "Título: " + title_value + "\nDescription: " + description_value)
    else:
        print(Fore.LIGHTGREEN_EX + "No se ha podido acceder a la informacion")
