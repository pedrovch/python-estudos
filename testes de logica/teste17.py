a = int(input('prmeiro numero: '))
b = int(input('segundo numero: '))

def mdc(a, b):
    resto = None
    while resto != 0:
        resto = a % b
        a  = b
        b  = resto

    return a
print(mdc(a, b))