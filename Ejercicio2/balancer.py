def is_balanced(expression):
    stack = []
    steps = []
    pairs = {')': '(', ']': '[', '}': '{'}
    left_chars = '([{'
    right_chars = ')]}'

    for char in expression:
        if char in left_chars:
            stack.append(char)
            steps.append(f"Push '{char}': Stack {stack}")
        elif char in right_chars:
            if not stack or stack[-1] != pairs[char]:
                steps.append(f"Caracter incorrecto: '{char}': Stack {stack}")
                steps.append("La expresión no está balanceada.")
                return False, steps
            stack.pop()
            steps.append(f"Pop '{char}': Stack {stack}")
    
    balanced = len(stack) == 0
    if balanced:
        steps.append("La expresión está balanceada.")
    return balanced, steps

def read_expressions_from_file(file_path):
    expressions = []
    with open(file_path, 'r') as file:
        for line in file:
            expressions.append(line.strip())
    return expressions
    