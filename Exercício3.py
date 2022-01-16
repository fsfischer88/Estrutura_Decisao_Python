# 1.	Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Informe seu sexo:  \nM = Masculino" "\n"
                                   "F = Feminino ")

if sexo == "M":
    print("Seu sexo é Masculino")
elif sexo == "F":
    print("Seu sexo é Feminino")
else:
    print("Sexo Inválido")