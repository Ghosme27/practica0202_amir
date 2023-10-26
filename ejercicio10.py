almacen=input('Introduzca su contraseña:')
repetir=input('Vuelva a introducirla:')
while repetir != almacen:
    print('no coinciden')
    repetir=input('vuelva a introducirla:')
if repetir==almacen:
    print('la contraseña coincide')