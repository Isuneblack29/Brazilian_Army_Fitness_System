print('PROGRAMA DE ALISTAMENTO MILITAR DO EXERCITO BRASILEIRO')

nome = input('Digite Seu Nome: ')
idade = int(input('Digite Sua Idade: '))
peso = float(input('Digite Seu Peso: '))
altura = float(input('Digite Sua Altura: '))


if (idade >= 18 and idade < 60) and (peso >= 60 and peso < 100) and (altura >= 1.7 and altura < 3):
    print(f'Parabéns {nome} Você Está Apto A Servir O Exercito Militar Brasileiro')
else:
    print('VOCÊ NÃO ESTÁ APTO A ENTRAR NO EXERCITO MILITAR BRASILEIRO')