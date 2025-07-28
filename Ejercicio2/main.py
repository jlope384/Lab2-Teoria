from balancer import *

def main():
    file_path = "Lab2\Ejercicio2\expresiones.txt"

    expressions = read_expressions_from_file(file_path)
        
    for i, expression in enumerate(expressions, start=1):
        print(f"\nExpresión {i}: {expression}")
        balanced, steps = is_balanced(expression)

        print("Pasos del algoritmo:")
        for step in steps:
            print(f"{step}")

        if not balanced:
            corrected = balance_expression(expression)
            print(f"\nExpresión corregida: {corrected}")
            is_balanced(corrected)
 

if __name__ == "__main__":
    main()
