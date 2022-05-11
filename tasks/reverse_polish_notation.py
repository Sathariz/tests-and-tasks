math_symbols = "+-*/"
numbers = "1234567890"

# str = "2+3-9+5*2-8/2"
str = "3+5*2"

def rpn(math):
    num_stack = []
    symbol_stack = []
    stack = []

    for char in math:
        if char in numbers:
            num_stack.append(char)
        
        if char in math_symbols:
            symbol_stack.append(char)

    num_stack.extend(reversed(symbol_stack))

    calculate = {
        "+" : lambda x,y: x + y,
        "-" : lambda x,y: x - y,
        "*" : lambda x,y: x * y,
        "/" : lambda x,y: x / y,
    }

    for char in num_stack:
        if char in numbers:
            stack.append(char)

        elif char in math_symbols:
            a = float(stack.pop(-1))
            b = float(stack.pop(-1))
            c = calculate[char](a, b)
            stack.append(c)

    return stack

print(rpn(str))