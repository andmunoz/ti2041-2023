# Función para el cálculo de la nota en base a la exigencia
def calcularNota(min, max, puntaje, exigencia):
    # Calculamos el puntaje de aprobación
    aprobacion = min + (max - min) * exigencia / 100
    m = 1
    n = 0

    # Caso del puntaje menor al de aprobación
    if puntaje < aprobacion: 
        m = 3.0 / (aprobacion - min)
        n = 1.0 - m * min

    # Caso del puntaje mayor al de aprobación
    if puntaje >= aprobacion:
        m = 3.0 / (max - aprobacion)
        n = 4.0 - m * aprobacion

    # Calculamos la nota real y la devolvemos
    nota = m * puntaje + n
    return nota

# Función para calcular las notas y generar la estructura de salida
def cargarEvaluacion(nombreArchivo, puntajeTotal, exigencia):
    # Lectura de las notas a memoria y cálculo de la nota final
    notas = []
    archivoNotas = open(nombreArchivo)
    for registro in archivoNotas:
        # Se lee cada línea del archivo y luego se separa en campos
        registro = registro.rstrip("\\n")
        campos = registro.split(sep = ';')

        # Creamos el diccionario con los valores iniciales de nota y puntaje
        notaAlumno = {
            "rut": campos[0],
            "nombre": campos[1],
            "puntaje": 0,
            "nota": 1.0 }

        # Calculamos el puntaje total obtenido por el alumno
        for i in range(2, len(campos)):
            notaAlumno["puntaje"] += int(campos[i])

        # Calculamos la nota en base a la exigencia ingresada
        notaAlumno["nota"] = round(calcularNota(0, puntajeTotal, notaAlumno["puntaje"], exigencia), 1)

        # Guardamos el diccionario en la lista de alumnos (notas)
        notas.append(notaAlumno)

    # Cerramos el archivo y devolvemos la estructura completa
    archivoNotas.close()
    return notas

# Solicitamos los valores para ejecutar la evaluación
nombreArchivo = input('Ingrese el nombre del archivo >> ')
puntajeTotal = input('Ingrese el total de puntos de la evaluación >> ')
exigencia = input('Ingrese la exigencia (por ejemplo: 60) >> ')

# Procesamos los datos
notas = cargarEvaluacion(nombreArchivo, int(puntajeTotal), int(exigencia))

# Mostramos en pantalla el resultado (sin formatear)
for alumno in notas:
    print(alumno)