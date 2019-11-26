for c in range(0, 151):
    if c % 7 == 0 and c % 11 == 0:
        print('multiplo de 7 e 11')
    elif c % 7 == 0 and c % 11 != 0:
        print('multiplo de 7')
    elif c % 7 != 0 and c % 11 == 0:
        print('multiplo de 11')
    else:
        print(c)

