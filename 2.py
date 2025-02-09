import re 
from collections import Counter

texto = input("escreva um breve texto: ")

palavras_apenas = re.sub(r'[^\w\s]', '', texto)
palavras_apenas = texto.split()

contagem = Counter(palavras_apenas)

print(contagem)