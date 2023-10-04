from django.shortcuts import render, HttpResponse

# Se llama con un valor para la variable page por default, así diferenciamos la vista final.
def index(request, page="index.html"):
    # Se define un contexto vacío
    context = {}

    # Se verifica el envío del formulario (independiente de la vista)
    if request.POST:
        page = request.POST['page']
        context['operador'] = request.POST['operador']
        
        # Caso de operación binaria, se obtienen los operandos
        context['operando1'] = float(request.POST['operando1'])
        context['operando2'] = float(request.POST['operando2'])

        # Se operan los operandos
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

    # Se renderiza la vista para mostrar el resultado
    return render(request, page, context)