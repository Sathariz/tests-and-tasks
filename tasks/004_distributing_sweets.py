#https://pl.spoj.com/problems/PRZEDSZK/
#how many sweets a lady from kindergarten should buy for kids to distribute them all
#no matter which class she'll teach and giving each kid the same amount

# code should tell what is the smallest common number for both given numbers

# first input is for how many times it should run
# next input is for two numbers divided by one space

def give_out_sweets():
    classes = ""
    resp = ""
    lst = []

    amount_of_runs = int(input("Amount: "))
    for _ in range(amount_of_runs):
        classes += input("")
        lst = classes.split(" ")
    
        a = int(lst.pop(0))
        b = int(lst.pop(0))

        mn_a = a
        mn_b = b
        while mn_a != mn_b:
            if mn_a > mn_b:
                mn_b += b

            else:
                mn_a += a

        resp += f"\n{mn_a} -> {int(mn_a/a)} | {int(mn_a/b)}"
        resp

    return resp

print(give_out_sweets())