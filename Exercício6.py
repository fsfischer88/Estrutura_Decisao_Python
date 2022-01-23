# 6. Faça um Programa que leia três números e mostre o maior deles.

numeros = []

def maior_numero():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))
    numeros.append(numero1)
    numeros.append(numero2)
    numeros.append(numero3)

    maior_numero = max(numeros)
    print("O maior número da lista é: ", maior_numero)

maior_numero()