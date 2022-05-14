#https://pl.spoj.com/problems/SKARBFI/
# given a strange map with numbers, read it's pattern and figure out the shortest route to the treasure
#
# first input  - how many times the code should run
# second input - how many tips are given
# third input  - tips: two numbers with single space between
#                first number indicates direction, second amount of steps
# directions:
# 0 - north  |  1 - south  |  2 - west  |  3 - east


def treasure_hunt():
    y = x = steps_y = steps_x = direction_y = direction_x = 0
    map_runs = []
    response = ""

    amount_of_runs = int(input("Runs: "))
    for _ in range(amount_of_runs):
        amount_of_tips = int(input("Tips: "))
        for _ in range(amount_of_tips):
            tip = input("")
            map_step = tip.split(" ")

            direction = int(map_step[0])
            steps = int(map_step[1])

            match direction:
                case 0: y += steps
                case 1: y -= steps
                case 2: x -= steps
                case 3: x += steps

        map_runs.append([y, x])

    for i in range(len(map_runs)):
        y = map_runs[i][0]
        x = map_runs[i][1]

        if x == 0 and y == 0:
            return "Well"

        if y < 0:
            direction_y = 1
            steps_y = -y
        elif y > 0:
            direction_y = 0
            steps_y = y

        if x < 0:
            direction_x = 2
            steps_x = -x
        elif x > 0:
            direction_x = 3
            steps_x = x

        if steps_y == 0:
            response += f"\n{direction_x} {steps_x}\n"
        elif steps_x == 0:
            response += f"\n{direction_y} {steps_y}\n"
        else:
            response += f"\n{direction_y} {steps_y}\n{direction_x} {steps_x}\n"

    return response

print(treasure_hunt())
