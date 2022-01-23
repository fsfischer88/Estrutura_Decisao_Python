# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []

def numeros_decrescente():
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    numero3 = int(input("Digite o terceiro numero: "))
    numeros.append(numero1)
    numeros.append(numero2)
    numeros.append(numero3)

    numeros.sort()
    print(numeros)

numeros_decrescente()