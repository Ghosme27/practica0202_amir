frase=input('Introduzca una frase:')
letra=input('introduzca una letra:')
cuenta=0
for i in frase:
    if i==letra:
        cuenta +=1
print('la letra {' '} aparece {' '} en la frase {' '}'.format(letra,cuenta,frase))
        