times = ('Palmeiras','Corinthians','Inter','Athletico-PR','Atlético-MG',
         'Fluminense','São Paulo','Flamengo','Santos','Botafogo','Avaí',
         'Red Bull Bragantino','Goiás','Ceará','Cuiabá','Coritiba',
         'América-MG','Atlético-GO','Juventude','Fortaleza')
print('-='*50)
print('Lista de times do brasileirão')
print(times)
print('-='*50)
print('Os primeiros 5 times')
print(f'{times[:5]}')
print('-='*50)
print('Os 4 ultimos são:')
print(times[-4:])
print('-='*50)
print(sorted(times))
print(f'O São Paulo está na {times.index("São Paulo")+1}ª Posição')