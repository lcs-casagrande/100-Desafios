nas=int(input('Qual ano você nasceu?'))
ida=-nas+2017
print('O aluno tem {} anos'.format(ida))
if ida<=9:
    print('Mirim')
elif ida<=14:
    print('Infantil')
elif ida<=19:
    print('Junior')
elif ida<=20:
    print('Sênior')
else :
    print("Master")
