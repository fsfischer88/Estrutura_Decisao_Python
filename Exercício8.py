# 8.	Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

precos = []


def produtos():
    produto1 = float(input("Informe o preço do produto1: "))
    produto2 = float(input("Informe o preço do produto2: "))
    produto3 = float(input("Informe o preço do produto3: "))
    precos.append(produto1)
    precos.append(produto2)
    precos.append(produto3)
    print(precos)
    menor_preco = min(precos)

    if menor_preco == produto1:
        print("Você deve comprar o produto1. ", menor_preco)

    elif menor_preco == produto2:
        print("Você deve comprar o produto2. ", menor_preco)
    else:
        print("Você deve comprar o produto3. ", menor_preco)

produtos()

    
