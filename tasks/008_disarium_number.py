#https://edabit.com/challenge/yvJbdkmKHvCNtcZy9
# disarium number
# "sum of its digits raised to their respective positions is the number itself"
# e.gg.: 75 -> 7^1 + 5^2

number = 75

def is_disarium(disar_num):
    original_number = disar_num
    t = 10
    lst = []
    result = 0

    while int(disar_num/t) != 0:
        t *= 10

    t /= 10
    smaller_num = int(disar_num/t)
    lst.append(smaller_num)
    disar_num -= smaller_num*t

    if int(disar_num) <= 9:
        lst.append(int(disar_num))

    for i in range(len(lst)):
        result += pow(lst[i], i+1)

    if result == original_number:
        return True
        
    return False

print(is_disarium(number))
