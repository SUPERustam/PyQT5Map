import requests
from config import API_KEY

# api key doesn't work
params_maps = {
    # 'key': API_KEY,
    'll': '37.630481,55.772105',
    'size': '550,450',
    'l': 'map'
}


class MyBadRequest(requests.exceptions.ConnectionError):
    pass


def get_map(params_maps):
    response = requests.get("https://static-maps.yandex.ru/1.x/", params=params_maps)
    with open("data/map.png", "wb") as file:
        file.write(response.content)
    if response.reason == 'Bad Request':
        raise MyBadRequest


get_map(params_maps)
