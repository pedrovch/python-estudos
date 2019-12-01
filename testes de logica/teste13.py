n = int(input('numero: '))

def mq(n):
    if n > 10:
        return  1
    elif n == 10:
        return  2
    else:
        return  3
if mq(n) == 1:
    print('maior que 10')
if mq(n) == 2:
    print(' é 10')
if mq(n) == 3:
    print('menor que 10')