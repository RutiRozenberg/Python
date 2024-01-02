import math


def find_primes(end):
    prime=set()
    if end>0:
        prime.add(0)
    if end>1:
        prime.add(1)
    for num in range(end):

        if num >2:

            for i in range(2, num):

                if (num % i) == 0:
                    break

            else:

                prime.add(num)
    return  prime

def sort_list(List1):
    List1.sort()
    return List1
