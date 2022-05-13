#https://edabit.com/challenge/NybeH5L7wFPYeynCn
# prints out three letters from given word, rotate by one and do it again till the word ends
# e.gg.: "round" -> "rou", "oun", "und"

# strng = "alphabet"
strng = "edabit"

def tri_letter_words(word):
    lst = []
    while len(word) >= 3:
        lst.append(word[0:3])
        word = word[1:]
    return lst

print(tri_letter_words(strng))