n = int(input('um numero: '))

def prim(n):
    d = 1
    while d < n-1:
        d = d + 1
        if n % d == 0:
            return False
if prim(n) == False:
    print(' numero não  é primo')
else:
    print('numero  é primo')