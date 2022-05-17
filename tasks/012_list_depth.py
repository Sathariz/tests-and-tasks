#https://edabit.com/challenge/nn7Na6zHLEHS9R8j2
# count the amount of list elements and elements within nested lists
# lst = [1, 2, 3, [2, 4, "q", 7]]
lst = ["a", "b", ["c", "d", ["e"]]]
def list_depth(lst):
    count = 0

    for ele in lst:
        if isinstance(ele, list):
            n = list_depth(ele)
            count += n
        count += 1

    return count
print(list_depth(lst))