#https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt
# when snake 'eats' it grows double it's size
# how many times can it eat before there will be no space for it in a  n*n -sized  field 
# n = 3
# def snakefill(n):
#     snake_len = 1
#     apple = 0
#     n *= n
#     while snake_len <= n:
#         snake_len += snake_len
#         apple += 1
#     return apple-1
# print(snakefill(n))


#https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb
# merge two lists and check if them combined are a consecutive sequence() - each digit is n+1
# don't care about negative numbers or duplicates
lst1 = [1, 4, 6, 5]
lst2 = [2, 7, 8, 9]
def consecutive_combo(lst1:list, lst2:list):
    lst1.extend(lst2)
    lst1.sort()
    n = len(lst1) - 1
    if lst1[0] + n == lst1[n]:
        return True
    return False

print(consecutive_combo(lst1, lst2))
