#https://edabit.com/challenge/gt9LLufDCMHKMioh2
# stuttering
# print out two first letters from given word followed by '...' two times,
# then whole word ending with '?'

# assume that the word has at least 2 letters

srt = "incredible"

def stutter(word):
    output = ""
    first_letters = word[0:2]

    for i in range(2):
        output += f"{first_letters}..."

    output += f"{word}?"
    return output

print(stutter(srt))