
#contador = 0

#while contador < 10:
#	print (contador)
#	contador += 1

contador_interno = 0
contador_externo = 0

while contador_externo < 10:
	while contador_interno < 10:
		print (contador_externo, contador_interno)
		contador_interno += 1
	contador_externo += 1
	contador_interno = 0
print ('Contador finalizado!')
