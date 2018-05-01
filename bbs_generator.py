from random import randint
from bbs import BBS
import prime

class BBS_Generator:
    def __init__(self, max, n):
        self.max = max
        self.n = n
        self.numbers_gen = []

    def __is_good_prime(self, number):
        return number % 4 == 3 and prime.miller_rabin(number)

    def __choose_prime_number(self):
        random = randint(3, self.max - 1)
        while not self.__is_good_prime(random):
            random = randint(3, self.max - 1)
        return random

    def generate_numbers(self, nb_to_generate):
        print("** Choose p prime number **")
        p = self.__choose_prime_number()
        print("==> p = ", p)
        print("** Choose q prime number **")
        q = self.__choose_prime_number()
        print("==> q = ", q)
        seed = randint(1, self.max - 1)
        bbs = BBS(p, q, seed)

        for _ in range(nb_to_generate):
            self.numbers_gen.append(bbs.get_random_int(self.n))
        print("** End generation BBS **")

    def print(self):
        i = 0
        for x in self.numbers_gen:
            print("number ", i, " random value = ", x)
            i += 1


#Max prime numbers = 50000 , generate a number on 10 bits
bbs = BBS_Generator(1000000, 64)
#Generate 100 random numbers
bbs.generate_numbers(100)
bbs.print()
