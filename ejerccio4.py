edad=int(input('introduzca su edad:'))
ingresos=float(input('introduzca su sueldo mensual'))
if edad<=16:
    print('no tienes que tributar')
elif edad>16 and ingresos>1000:
    print('Tiene que tributar')
else:
    print('no tienes que tributar')