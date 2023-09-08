from archivos import cargarEvaluacion

# Solicitamos los valores para ejecutar la evaluación
nombreArchivo = input('Ingrese el nombre del archivo >> ')
puntajeTotal = input('Ingrese el total de puntos de la evaluación >> ')
exigencia = input('Ingrese la exigencia (por ejemplo: 60) >> ')

# Revisar si tenemos que controlar un caso excepecional
try:
   puntajeTotal = int(puntajeTotal)
   exigencia = int(exigencia)
except ValueError: 
   puntajeTotal = 100
   exigencia = 60

# Procesamos los datos
notas = cargarEvaluacion(nombreArchivo, puntajeTotal, exigencia)

# Mostramos en pantalla el resultado (sin formatear)
for alumno in notas:
   print(alumno)