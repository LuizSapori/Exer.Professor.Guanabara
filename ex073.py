times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense','Atlético-MG',
         'Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','Ec Vitória','Coritiba',
         'Avaí','Ponte Preta','Atlético-GO')
pos = times.index('Chapecoense')
print(times)
print('==++=='*15)
print('Os 05 primeiros times.')
print(f'Os cinco primeiros são: {times[0:5]}')
print('==++=='*15)
print('Os 04 últimos colocados.')
print(f'Os 04 últimos colocados são: {times[-4:]}')
print('==++=='*15)
print('Times em ordem alfabética.')
print(f'Em ordem alfabética: {sorted(times)}')
print('==++=='*15)
print(f'A Chapecoense está em {pos+1} ° lugar')