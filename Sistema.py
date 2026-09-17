# Sistema de Votación

votos = {}  # Diccionario: id_votante -> opcion


def registrar_voto(id_votante, opcion):
    if id_votante in votos:
        print(f"Error: el votante {id_votante} ya votó.")
        return False

    votos[id_votante] = opcion
    print(f"Voto registrado para {id_votante}.")
    return True


def ver_resultados():
    total_votos = len(votos)

    if total_votos == 0:
        print("\nNo hay votos registrados.")
        return

    conteo = {}

    for opcion in votos.values():
        conteo[opcion] = conteo.get(opcion, 0) + 1

    print("\n=== RESULTADOS DE LA VOTACIÓN ===")

    for opcion, cantidad in conteo.items():
        porcentaje = (cantidad / total_votos) * 100
        print(f"- {opcion}: {cantidad} votos ({porcentaje:.2f}%)")

    print(f"Total de votos: {total_votos}")


def reiniciar_votacion():
    if not votos:
        print("\nNo hay votos para guardar.")
        return

    with open("historial_votaciones.txt", "a", encoding="utf-8") as archivo:
        archivo.write("=== VOTACIÓN ===\n")

        conteo = {}

        for opcion in votos.values():
            conteo[opcion] = conteo.get(opcion, 0) + 1

        total_votos = len(votos)

        for opcion, cantidad in conteo.items():
            porcentaje = (cantidad / total_votos) * 100
            archivo.write(
                f"{opcion}: {cantidad} votos ({porcentaje:.2f}%)\n"
            )

        archivo.write(f"Total de votos: {total_votos}\n")
        archivo.write("\n")

    votos.clear()

    print("\nLa votación fue reiniciada.")
    print("El historial fue guardado en 'historial_votaciones.txt'.")


def mostrar_menu():
    print("\n==============================")
    print("     SISTEMA DE VOTACIÓN")
    print("==============================")
    print("1. Registrar voto")
    print("2. Ver resultados")
    print("3. Reiniciar votación")
    print("4. Salir")
    print("==============================")


def main():
    while True:
        mostrar_menu()

        opcion_menu = input("Selecciona una opción: ").strip()

        if opcion_menu == "1":
            id_votante = input("Ingresa el ID del votante: ").strip()

            if not id_votante:
                print("Error: el ID no puede estar vacío.")
                continue

            opcion = input("Ingresa la opción por la que votas: ").strip()

            if not opcion:
                print("Error: la opción no puede estar vacía.")
                continue

            registrar_voto(id_votante, opcion)

        elif opcion_menu == "2":
            ver_resultados()

        elif opcion_menu == "3":
            confirmacion = input(
                "¿Seguro que quieres reiniciar la votación? (s/n): "
            ).strip().lower()

            if confirmacion == "s":
                reiniciar_votacion()
            else:
                print("Operación cancelada.")

        elif opcion_menu == "4":
            print("\nPrograma terminado.")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
