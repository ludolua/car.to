import random
import os
import json

with open("cars.json", encoding='utf8') as meu_json:
    data = json.load(meu_json)

nome = input("Olá, Qual seu nome?\n")

sim = f"{nome}, o seu contrato atual contempla o seguinte:\n"
não = f"{nome} deseja contratar um de nossos serviços?"

print(f"Olá, {nome}\n")
contrato = input("Possui algum contrato de aluguel de veiculo?\n[1] Sim\n[2] Não\n")

if contrato == "1":
    for i in data:
        print(sim)
        print(i['Modelo'])
        print(i['Ano'])
        print(i['Valor mensal'])
elif contrato == "2":
    print(não)
