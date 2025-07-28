# Precedencia de operadores
def get_precedence(c):
    precedences = {'(': 1, '|': 2, '.': 3, '?': 4, '*': 4, '+': 4, '^': 5}
    return precedences.get(c, 6)

# Formatea la expresión regular para insertar puntos entre operadores y operandos según las reglas de precedencia
def format_regex(regex):
    all_operators = ['|', '?', '+', '*', '^']
    binary_operators = ['|', '^']
    result = ''
    i = 0

    while i < len(regex):
        c1 = regex[i]

        # Si el carácter está escapado
        if c1 == '\\' and i + 1 < len(regex):
            result += c1 + regex[i + 1]
            i += 2
            continue

        result += c1

        if i + 1 < len(regex):
            c2 = regex[i + 1]

            # No insertar punto si c1 o c2 no lo permite
            if (c1 != '(' and c2 != ')' and
                c2 not in all_operators and
                c1 not in binary_operators and
                c2 != '|'):
                result += '.'
        i += 1

    return result

# Convierte de infix a postfix, paso a paso
def infix_to_postfix(regex):
    output = ''
    stack = []
    steps = []
    formatted = format_regex(regex)

    i = 0
    while i < len(formatted):
        c = formatted[i]

        if c == '\\' and i + 1 < len(formatted):  # carácter escapado
            escaped_char = formatted[i] + formatted[i + 1]
            output += escaped_char
            steps.append(f"Escapado: agregar '{escaped_char}' a la salida")
            i += 2
            continue

        if c == '(':
            stack.append(c)
            steps.append(f"Push '(' a la pila")
        elif c == ')':
            while stack and stack[-1] != '(':
                popped = stack.pop()
                output += popped
                steps.append(f"Pop '{popped}' de la pila a la salida")
            if stack and stack[-1] == '(':
                stack.pop()
                steps.append(f"Pop '(' de la pila")
        elif c in ['|', '.', '?', '*', '+', '^']:
            while (stack and get_precedence(stack[-1]) >= get_precedence(c)):
                popped = stack.pop()
                output += popped
                steps.append(f"Pop '{popped}' de la pila a la salida")
            stack.append(c)
            steps.append(f"Push operador '{c}' a la pila")
        else:
            output += c
            steps.append(f"Agregar operando '{c}' a la salida")
        i += 1

    while stack:
        popped = stack.pop()
        output += popped
        steps.append(f"Pop restante '{popped}' de la pila a la salida final")

    return output, steps

# Procesa el archivo de entrada línea por línea
def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                expresion = linea.strip()
                if not expresion:
                    continue
                print(f"\nExpresión infix: {expresion}")
                try:
                    postfix, pasos = infix_to_postfix(expresion)
                    print("Expresión postfix:", postfix)
                    print("Pasos:")
                    for paso in pasos:
                        print(" -", paso)
                except Exception as e:
                    print("Error procesando la expresión:", str(e))
    except FileNotFoundError:
        print(f"Archivo '{nombre_archivo}' no encontrado.")


if __name__ == "__main__":
    archivo_entrada = "C:/Users/jlope/Documents/UVG/Teoria/Lab2/Ejercicio3/expresiones.txt" #No funciono con la ruta relativa "Lab2\Ejercicio3\expresiones.txt"
    procesar_archivo(archivo_entrada)
