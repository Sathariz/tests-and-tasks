from collections import deque

entry = input("Gimme brackets of all kinds: ")
deq_stack = deque(entry)
top = deq_stack.popleft()

'''
    Doesn't work when two or more bracket sequences are entered one after another
     egg. ' {}[] '

    Uncommenting line 55-59 and commenting like 60 will make it work
    but will also break the overall functionality

    Returning correct response also doesn't work
'''
def check_brackets(stack:deque, top:str) -> str:

    opening_brackets = "([{"
    closing_brackets = ")]}"
    # m = "All works?"

    #ok so now we don't have any reasonable response back whether error or all merry
    while len(stack) != 0:
        if top in opening_brackets:
            match top:
                case "(":
                    closing_bracket_type = ")"
                case "[":
                    closing_bracket_type = "]"
                case "{":
                    closing_bracket_type = "}"
                case _:
                    # return "How could it even go this way"
                    raise Exception("How could it even go this way")
                    # m = "How could it even go this way"
                    # print("How could it even go this way")
                    # break

            # problem if given string has only single bracket
            if len(stack) != 0:
                new_top = stack.popleft()
            else:
                # break
                raise Exception("Stack is empty so I guess all went well?")
                # m = "Stack is empty"
                # print("Stack is empty")
                # break


            if new_top in closing_brackets and new_top != closing_bracket_type:
                # return "Wrong closing bracket"
                raise Exception("Wrong closing bracket")
                # m = "Wrong closing bracket"
                # print("Wrong closing bracket")
                # break

            elif new_top == closing_bracket_type and len(stack) != 0:
                next = stack.popleft()
                # uncomment it for {}[] to work but then break rest of the functionality
                # if next in opening_brackets and len(stack) != 0:
                #     check_brackets(stack, next)
                #     # we need to break the loop here too - how
                # else:
                #     break
                break

            elif new_top in opening_brackets:
                check_brackets(stack, new_top)

        elif top in closing_brackets and len(stack) > 1:
            top = stack.popleft()
            continue
        
        elif top not in opening_brackets or top not in closing_brackets:
            # return "Please enter brackets only"
            raise Exception("Please enter brackets only")
            # m = "Please enter brackets only"
            # print("Please enter brackets only")
            # break

        else:
            return "All works?"
            # return m
    

print(check_brackets(deq_stack, top))
