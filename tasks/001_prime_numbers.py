#https://pl.spoj.com/problems/PRIME_T/
# determinate if given number ia a prime number


num = 11

def prime_num(n):
    if n <= 9:
        if n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0:
            return "YES"

    else:
        if n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0:
            return "NO"

        else:
            return "YES"

print(prime_num(num))