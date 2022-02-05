
usuarioA = input('Cual es el nombre del primer usuario? ')
usuarioAedad = int(input(f'Cual es la edad de {usuarioA}? '))
usuarioB = input('Cual es el nombre del segundo usuario? ')
usuarioBedad = int(input(f'Cual es la edad de {usuarioB}? '))

if usuarioAedad > usuarioBedad:
	print (f'{usuarioA} es mayor que {usuarioB}!')
elif usuarioAedad < usuarioBedad:
	print (f'{usuarioA} es menor que {usuarioB}!')
else:
	print (f'{usuarioA} y {usuarioB} tienen la misma edad!')
