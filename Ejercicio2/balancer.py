def is_balanced(expression):
    stack = []
    steps = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    left_chars = '([{'
    right_chars = ')]}'

    for char in expression:
        if char in left_chars:
            stack.append(char)
            steps.append(f"Push '{char}': Stack {stack}")
        elif char in right_chars:
            if not stack or pairs[stack[-1]] != char:
                steps.append(f"\nCaracter incorrecto: '{char}': Stack {stack}")
                steps.append("La expresión no está balanceada.")
                return False, steps
            stack.pop()
            steps.append(f"Pop '{char}': Stack {stack}")
    
    balanced = len(stack) == 0
    if balanced:
        steps.append("La expresión está balanceada.")
    return balanced, steps


def balance_expression(expression):
    stack = []
    result = ''
    pairs = {')': '(', ']': '[', '}': '{'}
    inverse_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in inverse_pairs:
            stack.append(char)
            result += char
        elif char in pairs:
            if stack and stack[-1] == pairs[char]:
                stack.pop()
                result += char
            else:
                continue
        else:
            result += char

    while stack:
        opening = stack.pop()
        result += inverse_pairs[opening]

    return result

def read_expressions_from_file(file_path):
    expressions = []
    with open(file_path, 'r') as file:
        for line in file:
            expressions.append(line.strip())
    return expressions
    