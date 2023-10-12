from django.shortcuts import render, HttpResponse
from math import *

# Se llama con un valor para la variable page por default, así diferenciamos la vista final.
def index(request, page="index.html"):
    # Se define un contexto vacío
    context = {}

    # Se verifica el envío del formulario (independiente de la vista)
    if request.POST:
        page = request.POST['page']

        # Calculadora simple
        if page == 'simple.html':
            # Obtener el operador
            context['operador'] = request.POST['operador']
            
            # Obtener los operandos
            context['operando1'] = float(request.POST['operando1'])
            context['operando2'] = float(request.POST['operando2'])
        
            # Casos de las operaciones simples
            match context['operador']:
                case "adicion":
                    context['resultado'] = context['operando1'] + context['operando2']
                case "sustraccion":
                    context['resultado'] = context['operando1'] - context['operando2']
                case "multiplicacion":
                    context['resultado'] = context['operando1'] * context['operando2']
                case "division":
                    if context['operando2'] == 0:
                        context['resultado'] = 'Error: División por cero'
                    else: 
                        context['resultado'] = context['operando1'] / context['operando2']
                case _:
                    context['resultado'] = 'Error: Operación desconocida'

        # Calculadora básica y científica
        else:
            # Obtenemos la operación como genérica y fijamos los operadores disponibles
            operation = request.POST['screen']
            operators_binary = ['+', '-', '*', '/', '**']
            operators_unary = ['sqrt', 'sin', 'cos', 'tan', 'log', 'log10']

            # Resolvermos la operación unaria
            for i in reversed(range(0, len(operators_unary))):
                operation_components = operation.split(operators_unary[i])

                # Si encontramos la operación, calculamos y retornamos
                if len(operation_components) != len(operation):
                    context['resultado'] = eval(operation)
                    return render(request, page, context)

            # Resolvermos la operación binaria
            for i in reversed(range(0, len(operators_binary))):
                operation_components = operation.split(operators_binary[i])

                # Si encontramos la operación, calculamos y retornamos
                if len(operation_components) > 1: 
                    value2 = float(operation_components[1])
                    if value2 == 0:
                        context['resultado'] = 'Error: División por cero'
                    else:
                        context['resultado'] = eval(operation)
                    return render(request, page, context)

    # Se renderiza la vista para mostrar el resultado
    return render(request, page, context)