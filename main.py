'''
Beecrowd: Problema 1080
21/04/2024
Milena Pestana da Costa
'''

#Objetivo: Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.


maior = 0
posicao = 0

for i in range(100):
  n = int(input())
  if n > maior:
    maior = n
    posicao = i + 1
print(maior)
print(posicao)
