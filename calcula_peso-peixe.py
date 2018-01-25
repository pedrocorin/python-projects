peso = int(input('Informe o peso de peixes pescados: '))
excesso = peso - 50
multa = excesso * 4

if peso > 50:
    print('Você pescou {}Kg de peixe e com excesso de {}Kg, você pagará uma multa de R${:.2f}'.format(peso, excesso, multa))
elif peso <= 50:
    excesso = 0
    print('Você pescou {} Kg de peixe, com excesso de {}Kg, você não pagará multa.'.format(peso, excesso))

