import re
from collections import Counter

texto = input("Digite uma frase: ")

apenas_texto = re.sub(r'[^\w\s]', '', texto)
contador = Counter(re.findall(r'[aeiouAEIOU]', apenas_texto))

escolha = input("Digite 1 para visualizar a contagem de apenas uma vogal. \nDigite 2 para visualizar a contagem de todas.\n")

if escolha == '1':
    escolha1 = input("Qual vogal deseja verificar?\n").lower()
    if escolha1 in contador:
        print(f"A vogal '{escolha1}' aparece {contador[escolha1]} vezes.")
    else: print("Isso não é uma vogal, ou ela não aparece no texto informado.")
elif escolha == '2':
    print("Contagem de todas as vogais: ")
    for vogal, contagem in contador.items():
        print(f"{vogal}: {contagem}")
else: print("Inválido")
