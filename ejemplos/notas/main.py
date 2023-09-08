from archivos import cargarEvaluacion

# Solicitamos los valores para ejecutar la evaluación
nombreArchivo = input('Ingrese el nombre del archivo >> ')
puntajeTotal = input('Ingrese el total de puntos de la evaluación >> ')
exigencia = input('Ingrese la exigencia (por ejemplo: 60) >> ')

# Procesamos los datos
notas = cargarEvaluacion(nombreArchivo, int(puntajeTotal), int(exigencia))

# Mostramos en pantalla el resultado (sin formatear)
for alumno in notas:
   print(alumno)