n = int(input('diga um numero: '))

def div(n):
    if n % 2 == 0:
        return True
if div(n) == True:
    print(n, 'é par')
else:
    print(n, 'é impar')