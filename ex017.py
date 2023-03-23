import math
n1 = float(input("Digite o valor da cateto oposto: "))
n2 = float(input('Digite o valor do cateto adjacente: '))
print("Com cateto oposto {} e adjacente{} a hipotenusa é {:.2f}".format(n1,n2,math.hypot(n1,n2)))