a=int(input('introduzca un numero entero:'))
for i in range (1,a+1,2):   #la ultima posicion del parentesis hace que salte de 2 en 2
    for j in range(i,0,-2):  #la ultima posicion del parentesis hace que i disminuya de 2 en 2
        print(j,end=' ')
    print(' ')