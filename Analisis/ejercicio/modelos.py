trabajadores = []
trabajador = {}
CARGOS  = ['ceo','desarrollador','analista de datos']
tiposArchivo = ['json', 'csv', 'txt']
Descuentos = dict(AFP=0.12, Salud=0.07)
"""
    trabajador = dict(Nombre, Cargo, SueldoBruto, descuentoAFP, descuentoSalud, LiquidoPagar)
	trabajadores = [trabajador1,..., trabajador_n]
	CARGOS  = ['ceo','desarrollador','analista de datos']
	tiposArchivo = ['json', 'csv', 'txt']

"""
def validar_cargo(cargo:str) -> bool:
    return cargo in CARGOS