from collections import deque

# entry = input("Gimme brackets of all kinds: ")

# all commented code is for the covenience of testing
def check_brackets(stack) -> str:
    stack = deque(stack)

    opening_brackets = "([{"
    closing_brackets = ")]}"

    top = stack.popleft()
    open_brackets = []

    if "<" in stack or ">" in stack:
        # return "Sorry, we do not support angle brackets"
        return "Errors"

    if len(stack)%2 == 0:
        # return "Please enter brackets in pairs - they don't like to be on their own"
        return "Errors"
        
    while len(stack) >= 1:
        if top in opening_brackets:
            next = stack.popleft()
            match top:
                case "(":
                    closing_bracket_type = ")"
                case "[":
                    closing_bracket_type = "]"
                case "{":
                    closing_bracket_type = "}"

            if next in closing_brackets and next != closing_bracket_type:
                # return "Wrong closing bracket in the middle"
                return "Errors"

            elif next == closing_bracket_type and len(stack) >= 1:
                top = stack.popleft()
                continue

            elif next in closing_brackets and len(open_brackets) != 0:
                # return "Wrong closing bracket"
                return "Errors"

            elif next in opening_brackets:
                open_brackets.append(top)
                top = next
                continue

            elif next == closing_bracket_type and len(open_brackets) == 0:
                # return "Miracles!"
                return "Bracketastic!"

            else:
                # return "Something went wrong"
                return "Errors"

        elif top in closing_brackets and len(open_brackets) == 0:
            top = stack.popleft()
            continue

        elif top in closing_brackets:
            match top:
                case ")":
                    closing_bracket_type = "("
                case "]":
                    closing_bracket_type = "["
                case "}":
                    closing_bracket_type = "{"

            if closing_bracket_type == open_brackets[-1] and len(stack) >= 1:
                top = stack.popleft()
                open_brackets.pop()
                continue
            else:
                # return "Bracket Miracles!"
                return "Bracketastic!"

        else:
            # return "Please, enter only brackets - ()[]{}"
            return "Errors"

    if len(stack) == 0 and len(open_brackets) == 0:
        # return "Miracle happened"
        return "Bracketastic!"

    elif len(stack) == 0 and len(open_brackets) == 1:
        match top:
            case ")":
                closing_bracket_type = "("
            case "]":
                closing_bracket_type = "["
            case "}":
                closing_bracket_type = "{"

        if closing_bracket_type == open_brackets[0]:
            return "Bracketastic!"

        else:
            # return "Last closing bracket is wrong"
            return "Errors"

    else:
        return "Errors"


# print(check_brackets(entry))
