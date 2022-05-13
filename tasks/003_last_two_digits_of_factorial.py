#notdone

#https://pl.spoj.com/problems/FCTRL3/
# allows to choose how many times user wants to run it
# allows to choose what numbers to factorial
# still doesn't support returning two last digits

def factorial():
    i = 0
    sil = []
    resp = ""

    amount_of_runs = int(input("Amount of runs: "))
    while i != amount_of_runs:
        sil.append(int(input("n! - ")))
        i += 1

    for n in sil:
        if n <= 1:
            resp += f"\n{n}! = 1"

        else:
            calc = 1
            for k in range(1, n+1):
                calc *= k
            
            resp += f"\n{n}! = {str(calc)}"

    # t = 10
    # if int(calc/t) < 0:
    #     return 0, calc
    
    # while int(calc/t) > 10:
    #     t *= 10

    # print(f"cccc {int(calc/t)} {calc - int(calc/t) * 10}")


    return resp

print(factorial())