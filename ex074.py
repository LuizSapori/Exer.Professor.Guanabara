from random import sample
num = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
sorteio = sample(num,5)
print(tuple(sorteio))
print(f'O menor valor é {min(sorteio)} e o maior é {max(sorteio)}')