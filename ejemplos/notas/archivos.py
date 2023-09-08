from notas import calcularNota

# Función para calcular las notas y generar la estructura de salida
def cargarEvaluacion(nombreArchivo, puntajeTotal, exigencia):
    # Lectura de las notas a memoria y cálculo de la nota final
    notas = []
    archivoNotas = open(nombreArchivo)
    for registro in archivoNotas:
        # Se lee cada línea del archivo y luego se separa en campos
        registro = registro.rstrip("\\n")
        campos = registro.split(';')

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