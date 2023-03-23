valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor duplicado. Digite novamente!')
    continuar = str(input('Deseja continuar S/N: ').strip().upper())
    if continuar == "N":
        valores.sort()
        print(valores)
        break
print('Fim')