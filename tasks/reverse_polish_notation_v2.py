from collections import deque

# math = "2+3*5"
# math = "2+3-9+5*2-8/2"
math = "9-2*3+4-1*2+1-8"

priority = {
    "*" : 0,
    "/" : 0,
    "-" : 1,
    "+" : 1
}

def rpn():
    calculate = {
        "*" : lambda x, y: x*y,
        "/" : lambda x, y: y/x,
        "+" : lambda x, y: x+y,
        "-" : lambda x, y: x-y
        }
    output = []
    operators = deque()

    for character in math:
        if character.isnumeric():
            output.append(int(character))
            continue

        if priority[character] == 1:
            while len(operators) != 0 and priority[operators[-1]] == 0:
                # x = output.pop()
                # y = output.pop()
                # output.append(calculate[operators.pop()](x,y))
                output.append(operators.pop())

        operators.append(character)

    while len(operators) != 0:
        # x = output.pop()
        # y = output.pop()
        # output.append(calculate[operators.pop()](x,y))
        output.append(operators.pop())

    print(output)

rpn()
