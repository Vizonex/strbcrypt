import random
import string

from bcrypt import gensalt, hashpw


def random_string():
    return "".join(random.choices(string.printable, k=8))


def generate_sample():
    a, b = (random_string(), gensalt(5))
    return a, b, hashpw(a.encode("utf-8"), b)


if __name__ == "__main__":
    samples = [generate_sample() for s in range(10)]
    print(samples)
