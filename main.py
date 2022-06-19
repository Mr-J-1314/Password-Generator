from random import random
import string
import random
from pip import main

if __name__== "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    plen = int(input("Enter password length\n"))
    # since plen says it is a int() so no string should be input in plen.
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    # random.shuffle(s)
    # print(s)
    print("Your password is:")
    print("".join(random.sample(s, plen)))
    # print("".join (s[0:plen]))
