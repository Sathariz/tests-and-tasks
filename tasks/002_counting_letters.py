#https://pl.spoj.com/problems/FLAMASTE/
# if in given string of capital letters there is more than two of the same letter in a row,
# write that letter once and then how many of them is there in a row
# e.gg.: AAAABBCCC -> A4BBC3

# word = "AAAAAAAAAAAAATTTTTFRRDDDDDDDDFFFFFUUUUUJJJJHNNNNNNGGGGGGHHHHHFFFFFDDDDDSSRRRTYYYY"
word = "ABBCCCDDDDEEEEEFGGHIIJKKKL"

def words(s):
    count = 1
    new_str = ""

    for position, character in enumerate(s):
        if position+1 < len(s):
            if s[position+1] == character:
                count += 1
                continue

            new_str += character
            if count <= 2:
                new_str += character
            else:
                new_str += str(count)
            
            count = 1

        else:
            new_str += character
            if count != 1:
                new_str += str(count)

    return new_str

print(words(word))
