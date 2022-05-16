#https://edabit.com/challenge/2zKetgAJp4WRFXiDT
# get number length without using len()


def number_length():
    num = 0
    ten = 10
    n = 1

    if num < 0:
        num = -num

    while int(num/ten) != 0:
        ten *= 10
        n += 1

    return n

print(number_length())
