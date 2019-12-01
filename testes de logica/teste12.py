n = int(input('numero: '))

def sinal(n):
    if n >= 0:
        return True
    else:
        return False
if sinal(n) == True:
    print(n, 'é positivo')
else:
    print(n, 'é negativo')
