escolha = input("Qual forma geometrica deseja usar? (C)irculo, (Q)uadrado, (R)etangulo ou (T)riangulo: ")

if escolha == 1:
    raio = input("Digite o raio do circulo: ")
    area = 3.14 * raio
    print("A area do circulo e: ", area)
elif escolha == 2:
    base = input("Digite a base do retangulo: ")
    lado = input("Digite o lado do retangulo")
    area = base * lado
    print("A area do retangulo e: ", area)  
elif escolha == 3:
    base = input("Digite a base do triangulo: ")
    altura = input("Digite a altura do triangulo: ")
    area = (base * altura) / 2
    print("A area do triangulo e: ", area)
elif escolha == 4:
    lado = input("Digite o lado do quadrado: ")
    area = lado * lado
    print("A area do quadrado e: ", area)
elif escolha not in [1, 2, 3, 4]:
    print("Opcao invalida")

