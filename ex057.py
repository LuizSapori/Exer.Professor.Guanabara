sexo = str(input('Digite seu sexo (F/M): ')).strip().upper()[0]
while sexo not in 'FfMm':
    print('Dados invalidos. Por favor digite seu sexo corretamente: ')
    break
print('Próxima etapa.')