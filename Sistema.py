def reiniciar_votacion():
    if not votos:
        print("No hay votos para guardar.")
        return

    with open("historial_votaciones.txt", "a") as archivo:
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
    print("La votación fue reiniciada y el historial fue guardado.")
