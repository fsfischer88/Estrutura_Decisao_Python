# 1.	Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a 
# média alcançada por aluno e apresentar:
# o	A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# o	A mensagem "Reprovado", se a média for menor do que sete;
# o	A mensagem "Aprovado com Distinção", se a média for igual a dez.


notas = []

def media_aluno():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    notas.append(nota1)
    notas.append(nota2)
    media = sum(notas) / 2
    print(notas)
    print("Media: ",media)

    if media >= 7 and media < 10:
        print("Aprovado. Sua média foi: ", media)
    elif media == 10:
        print("Aprovado com Distinção. Sua média foi: ", media)
    else:
        print("Reprovado. Sua média foi: ", media)

media_aluno()
    


