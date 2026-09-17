🗳️ Sistema de Votación en Python
Aplicación desarrollada en Python para gestionar un proceso de votación de manera digital y en consola. Permite registrar votos de forma única por votante, calcular porcentajes en tiempo real, determinar al ganador (o manejar empates) y guardar un historial detallado en un archivo de texto.

🚀 Características Principales
Registro Único de Votos: Valida mediante el ID del votante que nadie pueda emitir más de un voto (id_votante).

Visualización Dinámica: Muestra el listado de opciones, la cantidad de votos recibidos y el porcentaje exacto que representa cada una respecto al total.

Detección de Ganador / Empates: Al consultar los resultados, el sistema identifica automáticamente la opción ganadora o avisa si hay un empate entre varias opciones.

Historial Persistente: Al reiniciar la votación, los resultados consolidados (incluyendo el ganador o empate y los porcentajes) se exportan automáticamente al archivo historial_votaciones.txt.

Interfaz de Menú Interactivo: Navegación sencilla en consola a través de opciones numéricas con validaciones de entradas vacías y errores.

📋 Funciones del Código
registrar_voto(id_votante, opcion)

Verifica si el ID del votante ya existe en el diccionario votos. Si ya votó, rechaza la operación; de lo contrario, almacena su voto.

ver_resultados()

Calcula el total de votos, agrupa el conteo por cada opción, calcula el porcentaje correspondiente, imprime los resultados formateados y evalúa quién es el ganador o si hubo empate.

reiniciar_votacion()

Guarda un resumen completo de la votación actual en el archivo historial_votaciones.txt con codificación UTF-8 y limpia el diccionario para iniciar un nuevo proceso.

mostrar_menu() / main()

Controla el flujo principal del programa mediante un bucle while y maneja las entradas del usuario con validaciones básicas de errores.

🛠️ Requisitos y Ejecución
Requisito: Tener instalado Python 3.x en tu equipo.