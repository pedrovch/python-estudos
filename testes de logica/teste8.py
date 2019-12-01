#custo final

custo_fab = 10000.00
p_dist = 0.28
p_imp = 0.45

def custo_final(custo_fab):
    a = custo_fab * p_dist
    b = custo_fab * p_imp
    return custo_fab + a + b
print('o custo final é:', custo_final(custo_fab))