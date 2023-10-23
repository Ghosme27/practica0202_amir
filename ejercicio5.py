sexo=input('diga su sexo poniendo H o M:')
nombre=input('introduzca su nombre:')
if sexo.upper()=='M' and nombre.upper()<'M':
    print('Tu casa es Gryffindorh')
elif sexo.upper()=='M' and nombre.upper()>'M':
    print('Tu casa es Slytheryn')
elif sexo.upper()=='H' and nombre.upper()>'N':
    print('Tu casa es Gryffindorh')
elif sexo.upper()=='H' and nombre.upper()<'N':
    print('Tu casa es Slytheryn')