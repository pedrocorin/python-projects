
sp = float(input('Informe quanto você ganha por hora: R$'))
hm = int(input('Informe quantas horas você trabalha por mês: '))
salario_bruto = sp * hm
ir = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sind = salario_bruto * (5/100)
salario_liquido = salario_bruto - ir - inss - sind
print('Seu salário bruto + : R$ {:.2f}'.format(salario_bruto))
print('Desconte Imposto de Renda -(11%): R$ {:.2f}'.format(ir))
print('Desconto INSS -(8%): R${:.2f}'.format(inss))
print('Desconto do Sindicato -(5%): R${:.2f}'.format(sind))
print('Salário Liquido: R${:.2f}'.format(salario_liquido))


