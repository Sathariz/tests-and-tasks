#https://edabit.com/challenge/SHdu4GwBQehhDm4xT
#
#

def jailbreak():
    # cells = [1, 0, 1, 1, 0, 1]
    # cells = [1, 1, 1]
    # cells = [0, 1, 1]
    cells = [1, 1, 0, 0, 0, 1, 0]
    # cells = [0, 0, 0]
    open_closed = 0
    freed = 1

    if cells[0] == 0:
        return 0

    for cell in range(1, len(cells)):
        if (cells[cell]+open_closed)%2 == 0:
            freed += 1
            open_closed += 1
        
    return freed

print(jailbreak())