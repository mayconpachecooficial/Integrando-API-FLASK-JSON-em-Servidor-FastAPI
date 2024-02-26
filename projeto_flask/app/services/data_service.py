import json

def get_data():
    # Substitua 'data/dados.json' pelo caminho correto do seu arquivo JSON
    with open('data/dados.json', 'r') as file:
        data = json.load(file)
    return data
