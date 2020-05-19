''' Implement pow(A, B) % C.

In other words, given A, B and C, find (AB)%C.

 

Input:

The first line of input consists number of the test cases.

 The following T lines consist of 3 numbers each separated by a space and in the following order:

A B C

'A' being the base number, 'B' the exponent (power to the base number) and 'C' the modular.

 

Output:

In each separate line print the modular exponent of the given numbers in the test case.


Constraints:

1 ≤ T ≤ 70

1 ≤ A ≤ 10^5

1 ≤ B ≤ 10^5

1 ≤ C ≤ 10^5


Example:

Input:

3
3 2 4
10 9 6
450 768 517

Output:

1
4
34
 '''

import sys
sys.setrecursionlimit(1500)
import time
start_time = time.time()


def updatedBigMod(baseN, exponent, modOf):
    if(exponent == 0):
        return 1
    if(exponent == 1):
        return baseN%modOf
    if (exponent%2 == 0):
        finalResult = updatedBigMod(baseN, int(exponent/2), modOf)
        return (finalResult*finalResult)%modOf
    else:
        finalResult = updatedBigMod(baseN, int(exponent/2), modOf)
        return (((finalResult*finalResult)%modOf)*baseN)%modOf



# def bigMod(baseN, exponent, modOf):
#     product = 1
#     for i in range(0, exponent):
#         product = product*baseN
#         finalMod = product % modOf
#     return(finalMod)




baseN = 450
exponent = 768
modOf = 517

# res = bigMod(baseN, exponent, modOf)
# print(res)

res = updatedBigMod(baseN, exponent, modOf)
print(res)

print("--- %s seconds ---" % (time.time() - start_time))


# submitted

# def updatedBigMod(baseN, exponent, modOf):
#     if(exponent == 0):
#         return 1
#     if(exponent == 1):
#         return baseN%modOf
#     if (exponent%2 == 0):
#         finalResult = updatedBigMod(baseN, int(exponent/2), modOf)
#         return (finalResult*finalResult)%modOf
#     else:
#         finalResult = updatedBigMod(baseN, int(exponent/2), modOf)
#         return (((finalResult*finalResult)%modOf)*baseN)%modOf

# T = int(input())

# for x in range(T):
#     res = [int(i) for i in input().split() if i.isdigit()] 
#     baseN = res[0]
#     exponent = res[1]
#     modOf = res[2]
#     result = updatedBigMod(baseN, exponent, modOf)
#     print(result)
