salario = float(input("Qual seu salário: "))
porcentagem = int(input("Quantos % de corte no salário: "))
descontos = float(input("Qual o valor dos descontos no contra-cheque: "))
descontos2 = float(input("Qual o valor dos descontos no contra-cheque: "))
if salario <= 2666.29:
    corte = (salario*porcentagem)/100
    empregador = salario-corte
    seguro = (salario-1599.61)*0.5
    governo = seguro+1279.69
    apagargoverno = (governo*porcentagem)/100
    total = empregador+apagargoverno
    print("Salário pago pelo empregador R$ {:.2f} \n "
          "Salário pago pelo governo R$ {:.2f} \n "
          "Salário total do trabalhador R$ {:.2f}".format(empregador,apagargoverno,total-descontos))
elif salario > 2666.29:
    corte = (salario*porcentagem)/100
    empregador=salario-corte
    seguro = 1813.03
    apagargoverno = (seguro*porcentagem)/100
    total = empregador + apagargoverno
    print(" Salário pago pelo empregador R$ {:.2f} \n "
          "Salário pago pelo governo R$ {:.2f} \n "
          "Salário total do trabalhador R$ {:.2f}".format(empregador, apagargoverno,total-descontos))
