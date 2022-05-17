#https://edabit.com/challenge/M47FDJLjfNoZ6k6gF
# find out in what cup (A, B or C) is the ball after swapping cups
# AC -> swap cups A nd C
# swap moves are to be indicated with capital letters
# cannot swap with itself

lst = ["AB", "BC", "CA", "BC", "AC", "BC"]
# lst = ["BA", "AC", "CA", "BC"]
def cup_swap(move_list:list):
    ball_position = "B"

    for move in move_list:
        if ball_position not in move:
            continue

        if move[0] == ball_position:
            ball_position = move[1]
            continue

        ball_position = move[0]

    return ball_position
print(cup_swap(lst))
