#while True:
 #   try:
    #     numero = int(input("Digite um número inteiro (0 sai): "))
     #   if numero == 0:
           # break
   # except Exception:
       # print("Valor inválido! Digite novamente!")

import random
for i in range(10):
    print(random.randint(1,10))


num = random.randint(1,5)


num_sort = random.randint(1,5)


chance = 0
while chance>= 3:
    num_escolha = int(input("Entre com o número inteiro"
                        " >= 1 e <= 5:"))

chance = 0
while chance>= 3:
    if num_escolha == num_sort:
        print("Você acertou!")
    else:
        print("Você errou!")
    chance += 1

from random import choice

frutas = ["uva", "pera", "maçã", "laranja"]
sorteio_fruta = choice(frutas)
escolha_fruta = input("Digite o nome de uma nova fruta: ")


