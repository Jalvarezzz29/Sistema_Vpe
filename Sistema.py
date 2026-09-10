# Sistema de Votación
votos = {}  # Diccionario para almacenar id_votante: opcion

def registrar_voto(id_votante, opcion):
    if id_votante in votos:
        print(f"Error: El votante {id_votante} ya votó.")
        return False
    votos[id_votante] = opcion
    print(f"Voto registrado para {id_votante}.")
    return True
