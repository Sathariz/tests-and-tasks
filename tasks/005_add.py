#notdone

#https://pl.spoj.com/problems/RNO_DOD/

def add():
    answer = 0
    # lst = []

    amount_of_runs = int(input("Amount: "))
    for _ in range(amount_of_runs):
        answer = 0
        amount_of_numbers = int(input("Numbers: "))

        # for i in range(amount_of_numbers):
        lst = input("").split(" ")
            # lst = int(amount_of_numbers.split(" "))

        for number in lst:
            answer += int(number)
        print(answer)



add()