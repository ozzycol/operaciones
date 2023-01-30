validado = False

#función para validar un dato
def validar(valor):
	return False #de momento está sin implementar y devolvemos siempre False

#mensaje para que el usuario sepa que le solicitamos un valor
print('Introduzca un valor, por favor: ', end='')

#bucle para pedir el valor
while not validado:
	valor = input("digite logitud de clave")
	valido = validar(valor)
	if not validado:
		print('Lo siento, el valor no es válido, vuelva a intentarlo: ', end='')
    else:
		print(f'El valor válido es {valor}.')

#a partir de aquí sabemos que el valor es válido y ya podemos utilizarlo
