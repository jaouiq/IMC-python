# entrada de dados
nome = input('Informe o seu nome:')
peso = float(input('Informe o seu peso:'))
altura = float(input('Informe a sua altura:'))

# como o IMC é calculado?
IMC = (peso/altura**2)

# resultado do IMC
print(f'O valor do IMC de {nome} é {IMC:,.2f}.')

# classifica o IMC do usuário
if IMC >= 30:
    print(f'{nome} é obeso(a).')
elif IMC >= 25:
    print(f'{nome} está com sobrepeso.')
elif IMC >= 18.5:
    print(f'{nome} está com peso normal.')
else:
    print(f'{nome} está abaixo do peso.')

