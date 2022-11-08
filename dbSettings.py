import json  # Usado para manipular arquivos json

import model_weather  # importa o arquivo modelos.py

weather_md = model_weather.Weather # importa o arquivo objetos.py


#  inserir um novo usuário no banco de dados weather.json
def insert(self):
    with open('weather.json', 'r') as f:
        data = json.load(f)
    data['weather'].append(self.__dict__)
    with open('weather.json', 'w') as f:
        json.dump(data, f)

# O serviço de select_temp deve retornar todos os dados com um filtro, exemplo temp < 20

def select_temp():
    map_temp = {}
    with open('weather.json', 'r') as f:
        data = json.load(f)
    for i in data['weather']:
        temp = float(i['temperature'])
        if temp < 20:
            map_temp[temp] = i
    return map_temp
