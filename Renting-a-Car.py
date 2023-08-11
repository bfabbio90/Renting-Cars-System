import os

# Simulando um sistema de aluguéis de carros

carros = [
        ("Chevrolet Tracker", 120),
        ("Chevrolet Onix", 90),
        ("Chevrolet Spin", 150),
        ("Hyundai HB20", 85),
        ("Hyundai Tucson", 120),
        ("Fiat Uno", 70),
        ("Fiat Mobi", 70),
        ("Fiat Pulse", 130),
]

alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    print("==========================")
    print("Lista de carros disponíveis:")
    print("==========================")

    print("")

    print("\n")
    for i, car in enumerate(lista_de_carros):
        print("[{}] Modelo: {} Preço: R${:.2F} / dia.".format(i, car[0], car[1]))
        
 
while True:
    os.system('cls')
    print("==========================")
    print("Bem vindo à locadora de carros")
    print("============================")
    print("")
    print("")
    print("O que você deseja fazer?")
    print("0 - Mostrar Portifólio de carros | 1 - Alugar Carro | 2 - Devolver um carro")
    op = int(input())

    

    if op == 0:
        os.system("cls")
        mostrar_lista_de_carros(carros)


    if op == 1:
        os.system("cls")
        mostrar_lista_de_carros(carros)
        print("")
        print("Qual carro você deseja alugar? Digite o código.")
        escolhido = int(input())
        print("Por quantos dias você deseja alugar o carro?")
        dias = int(input())
        print("Parabéns, você irá alugar o carro: {}, por: {} dias, e seu valor será: R${:.2F}.".format(carros[escolhido][0], dias, carros[escolhido][1]*dias))
        print("")
        print("Deseja continuar? Digite 0 para continuar / 1 para sair.")
        if int(input()) == 0:
            alugados.append(carros[escolhido][0])
            carros.pop(escolhido)
            os.system('cls')
            print(f'Carro alugado: {carros[escolhido][0]}')
            print("")

                          

    if op == 2:
        print(f'Deseja realmente devolver o carro {carros[escolhido][0]}? (Digite 0 para Sim / 1 para não:)')
        if int(input()) == 0:
            os.system('cls')
            alugados.pop()
            carros.append(carros[escolhido])    
            print("Carro devolvido à lista de portifólio de carros disponíveis.".format(carros[escolhido][0]))

    print("")    
    print("Deseja fazer mais alguma operação? (Digite 0 para continuar / 1 para sair.)")
    if int(input()) == 1:
        break
