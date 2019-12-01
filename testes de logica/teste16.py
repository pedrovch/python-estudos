n = int(input('um numero: '))
def soma (n):
    s = 0
    while n != 0:
        s   += n % 10
        n = int(n/10)

    return s

print(soma(n))