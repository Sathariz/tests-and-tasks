#Josephus
#https://edabit.com/challenge/L9Zh7dWsENnE9P6qc
#
# not done

def joseph():
    # n = 41
    n = 6
    lst = []
    number_to_pop = 1

    for i in range(1, n+1):
        lst.append(i)
    print(lst)

    while len(lst) != 1:
        last = lst[-1]

        if len(lst)%2 == 0:
            l = int(len(lst)/2)
        else:
            l = int(len(lst)/2)+1

        for _ in range(l):
            if number_to_pop >= l:
                break
            lst.pop(number_to_pop) ######
            # if number_to_pop+1 <= l+1:
            #     number_to_pop += 1
            number_to_pop += 1
    
        if last == lst[-1]:
            number_to_pop = 0
        else:
            number_to_pop = 1

    return lst

print(joseph())

# start with number you want
# hop by how many you want

# depending on X and Y
# pop 0 or -1 and proceed as usual
# 