from random import randint
from time import sleep
clientes = []
cliente = 0
idades = []
idade = 0
senhas = []
ordem = ["\n1 - Idade (Do mais velho para o mais novo)", "2 - Ordem de chegada (Senha)\n"]
loop = 0

quantCliente = input("Quantos clientes estão na fila?: ")

while loop < int(quantCliente):
    cliente = input("\nQual o nome do " + str(loop + 1) + "° cliente?: ")
    clientes.append(cliente)

    idade = input("Qual a idade do " + str(loop + 1) + "° cliente?: ")
    idades.append(int(idade))

    senha = randint(1, 9999)
    senhas.append(senha)

    print("\n" + cliente + " tem " + idade +  " anos e sua senha é: " + str(senha))

    loop+=1

for prio in ordem:
    print(prio)

prioridade = int(input("Como o cliente será chamado? "))

if prioridade == 1:
    print("\nO cliente mais velho tem " + str(max(idades)) + " anos")
    sleep(5)


else:
    print("\nA senha mais baixa é " + str(min(senhas)))
    sleep(5)

#print(clientes, idades, senhas)