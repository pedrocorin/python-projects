h = float(input('Informe sua altura (cm): '))
sexo = int(input('Digite 1, se você é homem, e 2, se você é mulher: '))
pih = (72.7*h) - 58
pim = (62.1*h) - 44.7
if sexo == 1:
    print('Com base em sua altura de {:.2f}cm, e como você é homem, seu peso ideal seria de {:.2f}kg '.format(h, pih))
    peso = float(input('Informe seu peso: '))
    if peso == pih:
        print('Você está dentro do peso recomendado')
    elif peso > pih:
        print('Você está acima do peso ideal! Fecha a boca, porra!!!')
    else:
        print('Você está abaixo do peso ideal. Coma mais um pouco.')
elif sexo == 2:
    print('Com base em sua altura de {:.2f}cm, e como você é mulher, seu peso ideal seria de {:.2f}kg'.format(h, pim))
    peso = float(input('Informe seu peso atual: '))
    if peso == pim:
        print('Você está dentro do peso recomendado!!')
    elif peso > pim:
        print('Vpcê está acima do peso ideal! Fecha a boca, porra!!!')
    else:
        print('Você está abaixo do peso ideal. Coma mais um pouco.')
else:
    print('Opção inválida!!!')
