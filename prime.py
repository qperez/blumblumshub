from random import randint

"""
Algorithm of Miller-Rabin
Implementation based on the following wikipedia page : 
https://fr.wikipedia.org/wiki/Test_de_primalit%C3%A9_de_Miller-Rabin
"""


def millerrabinwitness(a, n):
    # n must be => than 3 and a > 1
    if n < 3 or a <= 1:
        return False

    # compute n-1 = 2**s * d with d odd
    d = n - 1
    s = 0
    while s > 1:
        q, r = divmod(d, 2)
        if r == 1:
            break
        s += 1
        d = q
    if pow(a, d, n) == 1:
        return False  # n isn't a miller rabin witness
    for i in range(s):
        if pow(a, pow(2, i) * d, n) == n - 1:
            return False  # n isn't a miller rabin witness
    return True  # n is definitely composite


def millerrabin(n, k=10):
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = randint(2, n - 1)
        if millerrabinwitness(a, n):
            return False
    return True


print(millerrabin(1021))
print(millerrabin(4))

