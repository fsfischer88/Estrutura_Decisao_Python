# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ["a","e","i","o","u"]
consoantes = []


for n in vogais:
    letra = input("Digite uma letra: ")

    if letra != n:
        print("A letra que você digitou é uma consoante: ", letra)
        break
    else:
        print("A letra que você digitou é uma vogal: ", letra)
        break
    
    




