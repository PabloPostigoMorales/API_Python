import requests
from colorama import *


def posterSerie():
    url = "https://moviesminidatabase.p.rapidapi.com/series/id/tt0280249/"

    headers = {
        "X-RapidAPI-Key": "20f84019f0mshee865c33ed4221dp1c2e20jsnfc95cc0881a0",
        "X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    # Obtener el JSON de la respuesta
    data = response.json()

    if 'banner' in data['results']:
        banner_value = data['results']['banner']
        print(Fore.LIGHTGREEN_EX+f"Poster: {banner_value}")
    else:
        print("No se encuentra poster")