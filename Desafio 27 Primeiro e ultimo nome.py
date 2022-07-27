nome=str(input('Qal seu nome completo?')).strip().title()
print('Muito prazer em te conhecer!')
name=nome.split()
print('Seu primeiro nome é {}.' .format(name[0]))
print('Seu ultimo nome é {}.' .format(name[len(name)-1]))



