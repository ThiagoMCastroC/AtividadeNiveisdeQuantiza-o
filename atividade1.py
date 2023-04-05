from math import*
a=int(input('Insira o número de níveis de quantização:'))
b=2**a
if a<=0:
    print('Número de níveis de quantização inválido!')
else:
    print(f'O número de bits é {b}')
    for i in range(0,b):
        print('As combinações dos bits são:',bin(i))
