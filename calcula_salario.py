#Sistema python para Calcular Salario
#By Pedro Corin
vh = float(input('Informe o valor que você ganha por hora: R$'))
hm = int(input('Informe quantas horas você trabalha por mês: '))
he_meia = int(input('Informe o quantas horas extras de 50% tu fez: '))
vhe_meia = float(input('Informe o valor por hora extra de 50%: '))
salario = vh * hm
s_hora_extra = he_meia * vhe_meia
print('Trabalhando {} por mês, ganhando R${} por hora, seu salário é de R${:.2f}'.format(hm, vh, salario + s_hora_extra))

