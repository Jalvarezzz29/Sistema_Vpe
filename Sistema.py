# Sistema de Votación
votos = {}

def registrar_voto(id_votante, opcion):
    if id_votante in votos:
        print(f"Error: El votante {id_votante} ya votó.")
        return False
    votos[id_votante] = opcion
    return True

def ver_resultados():
    total_votos = len(votos)
    if total_votos == 0:
        print("No hay votos registrados.")
        return
    
    conteo = {}
    for opcion in votos.values():
        conteo[opcion] = conteo.get(opcion, 0) + 1
        
    print("Resultados de la votación:")
    for opcion, cantidad in conteo.items():
        porcentaje = (cantidad / total_votos) * 100
        print(f"- {opcion}: {cantidad} votos ({porcentaje:.2f}%)")
