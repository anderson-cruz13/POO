from doc_004_a import CAMINHO_ARQUIVO, People
import json

with open(CAMINHO_ARQUIVO, 'r') as file:
    people_date = json.load(file)
    p1 = People(**people_date[0])

    print(p1.name)