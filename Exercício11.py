# 2.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
# para desenvolver o programa que calculará os reajustes.
# o	Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:
# o	salários até R$ 280,00 (incluindo) : aumento de 20%
# o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# o	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o	o salário antes do reajuste;
# o	o percentual de aumento aplicado;
# o	o valor do aumento;
# o	o novo salário, após o aumento.



def aumento_salarial_2022():
    salario = float(input("Informe o seu salario: "))
    print("Seu salário atual é :",salario)

    if salario <= 2800:
        aumento = salario * 0.20
        novo_salario = salario * 1.2
        print("Reajuste de 20%")
        print("Seu aumento foi de: ", aumento)
        print("Seu novo salário é: ", novo_salario)
    elif salario > 2800 and salario < 7000:
        aumento = salario * 0.15
        novo_salario = salario * 1.15
        print("Reajuste de 15%")
        print("Seu aumento foi de: ", aumento)
        print("Seu novo salário é: ", novo_salario)
    elif salario >= 7000 and salario <= 15000:
        aumento = salario * 0.10
        novo_salario = salario * 1.10
        print("Reajuste de 10%")
        print("Seu aumento foi de: ", aumento)
        print("Seu novo salário é: ", novo_salario)
    elif salario > 7000:
        aumento = salario * 0.05
        novo_salario = salario * 1.05
        print("Reajuste de 5%")
        print("Seu aumento foi de: ", aumento)
        print("Seu novo salário é: ", novo_salario)
    else:
        print("Seu salário não teve reajuste.")
aumento_salarial_2022()
    

