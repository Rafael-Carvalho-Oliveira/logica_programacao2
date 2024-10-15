
import random
import os
import time

lista_premiado = random.randint(1,100)
num_tentados = []

#Introdução
os.system("cls")
print(60*"#")
time.sleep(1.1)
print("Bem vindo ao jogo da adivinhação!")
time.sleep(1.1)
print("Você terá apenas 5 tentativas para acertar!")
time.sleep(1.1)
print("Escolha um número entre 1 e 100!")
time.sleep(1.1)
print(60*"#")
time.sleep(0.5)
print()

#Tempo de espera
time.sleep(1.3)

#O jogo

while True:
    print()
    ent_usuario = int(input("Digite um número: "))
    if ent_usuario == lista_premiado:
        os.system("cls")
        print("Você acertou!")
        break
    else:
        num_tentados.append(ent_usuario)
        if len(num_tentados) == 10:
           os.system("cls")
           print("Você atingiu o limite máximo de tentativas")
           print("Você perdeu! Boa tentativa!")
           break
         
        os.system("cls")
        print("Você Errou!")
        print(f"você já tentou os números {num_tentados}")
        if ent_usuario > lista_premiado:
              print("O número escolhido é menor!")
        else:
            print("O número escolhido é maior!")
   
print("Fim do jogo")

#Relatório final
print(f"O número premiado era {lista_premiado}")
print(f"Os números usados foram {num_tentados}")
print(f"Você conseguiu fazer com {len(num_tentados)} tentativas")