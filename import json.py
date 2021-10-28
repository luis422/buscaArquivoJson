import json
import os

pastas = os.listdir()
arquivos = []

for i in range(0,len(pastas)-1):
    arquivos.append(f"{pastas[i]}/project.json")

#print(arquivos)
print("Pastas lidas")

for i in range(0,len(arquivos)-1):
    try:
        with open(arquivos[i]) as f:
            data = json.load(f)
        print(f"Arquivo de projeto encontrado! {data['title']} na pasta '{pastas[i]}'")
    except(FileNotFoundError):
        print(f"Sem arquivo de projeto na pasta '{pastas[i]}'")
