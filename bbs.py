class BBS:
    """
    p is prime number
    q is a prime number
    seed is the x0
    mfactor is compute by p * q
    """

    def __init__(self, p, q, seed):
        self.p = p
        self.q = q
        self.seed = seed
        self.xn = seed
        self.mfactor = p * q

    """
    generation of bits string, n is the lenght of the number to generate in bits
    """

    def getrandom(self, n):
        out = ''
        for i in range(n):
            self.xn = pow(self.xn, 2, self.mfactor)
            out += str(self.xn % 2)
        return out

    """
    The same as above but return the value as an integer
    """

    def getrandomint(self, n):
        return int(self.getrandom(n), 2)


bbs = BBS(16217, 15629, 5081)
for i in range(100):
    print(bbs.getrandomint(10))
