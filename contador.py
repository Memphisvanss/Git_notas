from operator import truediv
from xmlrpc.client import Boolean

inicio = True
print ('Este es un contador, puedes contar hasta el numero que quieras en multiplos que quiereas, incluso en decimales.')
print ('Asegurate de siempre usar numeros, el programa aun no puede validar si es un numero o un caracter')
print ('Intentalo las veces que quieras. Que te diviertas!')
while inicio: #while principal, hace que el programa fuincione mientras que se le pida
    contador = float(input('Hasta que numero quieres contar?: '))
    multiplo = float(input('De cuanto en cuantos quieres contar?: '))
    a = multiplo
    b = 0
    while a <= contador: #While contador, es quien hace la cuenta
        print(a)
        a += multiplo
        b += 1
    print (f'Contador finalizado, se contaron: {b}!\n')
    valida = True
    while valida: #While validador, revisa que la respuesta sea valida
        respuesta = input('¿Quieres contar de nuevo? si o no: ')
        print ('\n')
        if respuesta == ('si'):
            respuesta = True
            valida = False
        elif respuesta == ('no'):
            respuesta = False
            valida = False
        else:
            print('Respuesta no valida, intenta de nuevo')
            valida = True
    inicio = respuesta