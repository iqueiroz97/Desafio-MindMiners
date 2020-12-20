from random import randint
clientes = []
cliente = 0
idades = []
idade = 0
senhas = []
tOper = ["1 - Idade (Do mais velho para o mais novo)", "2 - Ordem de chegada (Senha)"]
loop = 0

quantCliente = input("Quantos clientes estão na fila?: ")

while loop < int(quantCliente):
    cliente = input("Qual o nome do " + str(loop + 1) + "° cliente?: ")
    clientes.append(cliente)

    idade = input("Qual a idade do " + str(loop + 1) + "° cliente?: ")
    idades.append(int(idade))

    senha = randint(1, 9999)
    senhas.append(senha)

    print(cliente + " tem " + idade +  " anos e sua senha é: " + str(senha))

    loop+=1

prioridade = int(input("Como o cliente será chamado? "))

for prio in tOper:
        print(prio)

if prioridade == 1:
    print(max(idades, key=int))

#print(clientes, idades, senhas)