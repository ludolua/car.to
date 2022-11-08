import random
import os
import json

with open("cars.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)



nome = input("Olá, Qual seu nome?\n")

print(f"Olá, {nome}\n")
input("Possui algum contrato de aluguel de veiculo?\n")

sim = print(f"O seu contrato atual contempla o seguinte:\n")
não = input(f"{nome} deseja contratar um de nossos serviços?")
for i in dados:
    print(i['Carro'])
    print(i['Ano'])
    print(i['Valor mensal'])

