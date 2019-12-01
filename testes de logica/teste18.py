m = int(input('prmeiro numero: '))
n = int(input('segundo numero: '))

def mdc(n, m):
    a = n
    b = m
    resto = None
    while resto != 0:
        resto = a % b
        a  = b
        b  = resto

    return (n*m) / a 
print(mdc(n, m))