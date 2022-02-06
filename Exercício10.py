# 2.	Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou 
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
#  conforme o caso


def turno_estudos():
    turno = input("Em que turno você estuda? (M- Matutino \n V-Vespertino ou \n N-Noturno \n")
    if turno == "M":
        print("Matutino")
    elif turno == "V":
        print("Vespertino")
    elif turno == "N":
        print("Noturno")
    else:
        print("Você não digitou um turno válido")
turno_estudos()



    





