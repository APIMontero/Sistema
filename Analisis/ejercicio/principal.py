import metodos as fn
import modelos as mo
def menu() -> int:
	opcion = " "
	
	menu = """
	¡Bienvenido al sistema!

	Opciones
	--------
	1. Registrar Trabajador
	2. Listar Todos Los Trabajadores
	3. Imprimir Planilla De Sueldos
	4. Salir del programa

"""
	print(menu)
	opcion = input('Ingrese su opción(1-4): ')
	if not fn.is_numeric(opcion):
		return -1  # left range Error 
	else:
		# Correct Range 
		if int(opcion) in range(1,5):
			return int(opcion) 
		else:
			# right range Error 
			return 0

def ejercicio():
	while True:
		fn.cls()
		opcion = menu()  # (-1, 0, 1...4)
		if opcion == -1:
			print("Se debe ingresar un valor númerico.")
		elif opcion == 0:
			print("Opción No Válida. Debe estar comprendida entre 1 y 4.")
		else:
			# Llamar los metodos de acuerdo al numero del menu de opciones.
			if opcion == 4:
				# OK
				fn.cls()
				print("Ha finalizado correctamente el  programa.")
				fn.wait()
				fn.cls()
				break
			elif opcion == 1:
				# OK
				fn.registrar(mo.trabajadores)
				fn.wait()
			elif opcion == 2:
				# OK 
				fn.listar(mo.trabajadores)
				fn.wait()
			elif opcion == 3:
				# OK
				fn.planilla(mo.trabajadores)
				fn.wait()
			else:
				print("Opción No Válida")
			
		# ...


def main():
	ejercicio()

if __name__ == '__main__':
	main()

