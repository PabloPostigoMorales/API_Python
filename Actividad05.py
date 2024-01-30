import requests
from colorama import *


def peliculasNacimiento():
    print(Fore.BLUE + "Peliculas Registradas en 1982: ")
    url = "https://moviesminidatabase.p.rapidapi.com/movie/byYear/1982/"

    headers = {
        "X-RapidAPI-Key": "20f84019f0mshee865c33ed4221dp1c2e20jsnfc95cc0881a0",
        "X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    if 'count' in data:
        num_pelis = data['count']
        print(Fore.LIGHTGREEN_EX + f"Número de películas de ese año: {num_pelis}")
    else:
        print("No se encuentran películas de ese año")
