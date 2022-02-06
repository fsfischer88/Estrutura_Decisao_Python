# 2.	Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são 
# do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato 
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# o	Desconto do IR:
# o	Salário Bruto até 900 (inclusive) - isento
# o	Salário Bruto até 1500 (inclusive) - desconto de 5%
# o	Salário Bruto até 2500 (inclusive) - desconto de 10%
# o	Salário Bruto acima de 2500 - desconto de 20%.
#  Imprima na tela as informações, dispostas conforme 
# o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# o	        Salário Bruto: (5 * 220)        : R$ 1100,00
# o	        (-) IR (5%)                     : R$   55,00  
# o	        (-) INSS ( 10%)                 : R$  110,00
# o	        FGTS (11%)                      : R$  121,00
# o	        Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

def imposto_renda():
    horas_trab = float(input("Informe as horas trabalhadas no mês: "))
    vlr_hora = float(input("Informe o valor hora trabalhada: "))
    salario = horas_trab * vlr_hora
    print("Salário Bruto:          R$",salario)


    if salario <= 900:
        print("(-) IR (0%)           : R$ ISENTO")
        desc_inss = salario * 0.10
        print("(-) INSS(10%)        : R$ ",desc_inss)
        desc_fgts = salario * 0.11
        print("(-) FGTS(11%)        : R$ ",desc_fgts)
        total_desc = desc_inss
        print("Total de descontos    : R$ ",total_desc)
        salario_liq = salario - total_desc
        print("Salário Liquido       : R$ ",salario_liq)

    elif salario <= 1500:
        desconto_IR = salario * 0.05
        print("(-) IR (5%)           : R$ ", desconto_IR)
        desc_inss = salario * 0.10
        print("(-) INSS(10%)        : R$ ",desc_inss)
        desc_fgts = salario * 0.11
        print("(-) FGTS(11%)        : R$ ",desc_fgts)
        total_desc = desconto_IR + desc_inss
        print("Total de descontos    : R$ ",total_desc)
        salario_liq = salario - total_desc
        print("Salário Liquido       : R$ ",salario_liq)

    elif salario <= 2500:
        desconto_IR = salario * 0.10
        print("(-) IR (10%)          : R$ ", desconto_IR)
        desc_inss = salario * 0.10
        print("(-) INSS(10%)        : R$ ",desc_inss)
        desc_fgts = salario * 0.11
        print("(-) FGTS(11%)        : R$ ",desc_fgts)
        total_desc = desconto_IR + desc_inss
        print("Total de descontos    : R$ ",total_desc)
        salario_liq = salario - total_desc
        print("Salário Liquido       : R$ ",salario_liq)

    else:
        desconto_IR = salario * 0.20
        print("(-) IR (20%)          : R$ ", desconto_IR)
        desc_inss = salario * 0.10
        print("(-) INSS(10%)        : R$ ",desc_inss)
        desc_fgts = salario * 0.11
        print("(-) FGTS(11%)        : R$ ",desc_fgts)
        total_desc = desconto_IR + desc_inss
        print("Total de descontos    : R$ ",total_desc)
        salario_liq = salario - total_desc
        print("Salário Liquido       : R$ ",salario_liq)

imposto_renda()


    

