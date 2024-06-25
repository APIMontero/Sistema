import os
import modelos as mo

def registrar(trabajadores: list):
    cls()
    print('Registrar Trabajador')
    # Pedir data y validar
    nombre = input('Ingrese nombre y apellido del trabajador: ')

    cargo = " "
    while not mo.validar_cargo(cargo):
        cargo = input(f'Ingrese cargo del trabajador{tuple(mo.CARGOS)}: ').lower()
    
    sueldo_bruto = " "
    while not is_numeric(sueldo_bruto):
        sueldo_bruto = input('Ingrese el sueldo bruto del trabajador: $')
    # Calcular los otros atributos
    descuento_AFP = int(sueldo_bruto) * mo.Descuentos['AFP']
    descuento_salud = int(sueldo_bruto) * mo.Descuentos['Salud']
    total_descuentos = (descuento_AFP + descuento_salud)
    liquido_a_pagar = int(sueldo_bruto) - total_descuentos
    trabajadores.append({
        'Nombres':nombre, 
        'Cargo':cargo, 
        'SueldoBruto': sueldo_bruto,
        'DescuentoAFP': descuento_AFP,
        'DescuentoSalud': descuento_salud,
        'LiquidoPagar':liquido_a_pagar
    })

    print("Se ha completado el registro del nuevo trabajador.")
    

def listar(trabajadores) -> None:
    cls()
    print("Listado de Trabajadores.")
    print(f"{'Trabajador'}\t{'Cargo'}\t{'Sueldo Bruto'}\t{'Descuento AFP'}\t{'Descuento Salud'}\t{'Liquido a Pagar'}")
    for trabajador in trabajadores:
        print(f"{trabajador['Nombres']}\t{trabajador['Cargo']}\t{trabajador['SueldoBruto']}\t{trabajador['DescuentoAFP']}\t{trabajador['DescuentoSalud']}\t{trabajador['LiquidoPagar']}")
    return


def planilla(trabajadores):
    cls()
    # Tipo de archivo es txt
    tipoArchivo = mo.tiposArchivo[2]
    # Generar Archivo de acuerdo a necesidad del cliente 
    print("Imprimir Planilla De Sueldos.")
    opcion = input(f"Enter para ver immprimir todos los trabajadores o indique el cargo{tuple(mo.CARGOS)}: ").lower()
    # Diferenciar por todos o cargos
    filePart = ""
    if opcion in mo.CARGOS:
        filePart = f"planilla_{opcion}."
    elif opcion == "":
        filePart = f"planilla_{'todos'}."

    # Nombre completo del documento a generar
    filePart = filePart + tipoArchivo

    # Creación del archivo fisico
    with open(filePart, 'w', encoding='utf-8') as archivo:
        archivo.write('Planilla De Sueldo De Trabajadores\n\n')  # Titulo
        archivo.write(f"{'Trabajador'}\t{'Cargo'}\t{'Sueldo Bruto'}\t{'Descuento AFP'}\t{'Descuento Salud'}\t{'Liquido a Pagar'}\n")  # Cabeceras
        for trabajador in trabajadores:  # Cuerpo
            if trabajador['Cargo'] == opcion:
                archivo.write(f"{trabajador['Nombres']}\t{trabajador['Cargo']}\t{trabajador['SueldoBruto']}\t{trabajador['DescuentoAFP']}\t{trabajador['DescuentoSalud']}\t{trabajador['LiquidoPagar']}\n")
            elif opcion == "":
                archivo.write(f"{trabajador['Nombres']}\t{trabajador['Cargo']}\t{trabajador['SueldoBruto']}\t{trabajador['DescuentoAFP']}\t{trabajador['DescuentoSalud']}\t{trabajador['LiquidoPagar']}\n")
    
    print(f"Archivo '{filePart}' creado con éxito.")


def is_numeric(value:str) -> bool:
    correcto = False
    try:
        valor = float(value)
        correcto = True
    except Exception:
        pass
    finally:
        return correcto


def cls():
    os.system("clear")


def wait():
    input('Pulse una tecla para continuar...   ')

