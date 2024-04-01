from Crypto.Util.number import getStrongPrime, bytes_to_long
from hashlib import md5
import random
import os

secret = list(map(int,f"{bytes_to_long(os.urandom(16)):0104b}"[-100:]))
p = getStrongPrime(2048)
g = bytes_to_long(os.urandom(2048//8))

def game(seed):
    seed = md5(seed).digest()
    for i in range(15):
        seed = seed + md5(seed).digest()
    seed = bytes_to_long(seed)
    seed = pow(g,seed,p)
    r = random.Random()
    r.seed(seed)
    answer = ''.join(str(r._randbelow(2))for _ in range(100))
    guess = input()
    return (answer == guess,answer)

def main():
    used = set()
    for _ in range(16):
        seed = bytes.fromhex(input())
        if seed in used:
            print("You cannot reuse seed!")
            return
        used.add(seed)
        result, answer = game(seed)
        if result:
            print("Success!")
            with open("flag.txt","r") as f:
                print(f.read())
                return
        else:
            print("Failed!")
            print("Answer was:",answer)
main()