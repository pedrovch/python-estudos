#todos meses tem 30 dias

m = 30
n = int(input('numero de meses: '))
def total(m):
    return m * n
print(' o numero de dias em {} meses é: {}'.format(n, total(m)))