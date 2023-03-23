l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro Lado: '))
if l1 < l2 + l3 or l2 < l1 + l3 or l3 < l1+l2:
    print('Não é possível formar um triângilo. ')
    if l1 == l2 == l3:
        print("EQUILÁTERO!!! ")
    elif l1 != l2 != l3 != l1:
        print(" ESCALENO!! ")
    else:
        print("ISÓSCELES!!")
else:
    print('Não é possivel formar um triângulo')

#---------------ou---------------------------------------------------
#if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1+l2:
    #print('Não é possível formar um triângilo. ')
#elif l1 == l2 or l1 == l3 or l2 == l3:
    #print("Temos dois lados iguais. O trinagulo é isósceles. ")
#elif l1 != l2 and l1 != l3 and l2 != l3:
    #print(" Os três lados são diferentes. Temos um triângulo escaleno. ")
#elif l1==l2 and l1 == l3:
    #print("Os lados sãq iguais. O triangulo é equilatero.")
