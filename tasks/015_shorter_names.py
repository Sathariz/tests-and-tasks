#https://pl.spoj.com/problems/WI_IDEN/

def cut_short():
    vowels = "AIEOUYaieouy"
    n = int(input())
    # long_name = input()
    # long_name = "ALA_MA_KOTA_I_2_PSY"
    long_name = "sd__3_d5__$_26_h"
    lst = []
    output = ""

    numbers_list = "1234567890"

    # iterators for diferent loops
    character_position = -1
    number_position = -1
    vowel_position = 1


    if len(long_name) <= n:
        return long_name

    for c in long_name:
        lst.append(c)

    while len(lst) > n:
        # remove character if it isn't a number, letter or $
        if "_" in lst:
            if not lst[character_position].isalpha() and not lst[character_position].isnumeric() and lst[character_position] != "$":
                lst.pop(character_position)
                continue
            character_position -= 1
            continue

        # remove numbers going from the end
        if any(numb in lst for numb in numbers_list):
            if lst[number_position].isnumeric():
                lst.pop(number_position)
                continue
            number_position -= 1
            continue

        if any(c in lst for c in vowels) and vowel_position < n:
            for character in vowels:
                if lst[vowel_position] == character:
                    lst.pop(vowel_position)
                    continue
            vowel_position += 1
            continue

        lst = lst[:n]

    for j in lst:
        output += j
    print(output)
    
cut_short()
