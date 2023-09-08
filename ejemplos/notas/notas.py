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