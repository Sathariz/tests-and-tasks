#https://edabit.com/challenge/MfypAQedEAun4oQFA

lst = [3, 0, 2]
i = 0
n = 26

while len(lst) != n+1:
    lst.append(lst[i] + lst[i+1])
    i += 1
print(lst[n])