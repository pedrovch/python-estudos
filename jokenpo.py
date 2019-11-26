from random import randint

intens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print(''' escolha:
PEDRA [1]
PAPEL [2]
TESOURA[3]
''')
jogador = (int(input('quala  sua jogada? ')))
print('você jogou: {}'.format(intens[jogador]))
print('o computador jogou: {}'.format(intens[computador]))
