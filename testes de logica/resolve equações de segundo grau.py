import math
a = int(input('valor de a: '))
b = int(input('valor de b: '))
c = int(input('valor de c: '))

def delta(a, b, c):
    return b*b  - 4 * a * c
def raiz1(a, b, c):
    return (-b + math.sqrt(delta(a, b, c))) / 2 * a
def raiz2(a, b, c):
    return (-b - math.sqrt(delta(a, b, c))) / 2 * a


print(delta(a, b, c))
print(raiz1(a, b, c))
print(raiz2(a, b, b))