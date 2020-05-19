import math

num = int(input("How many terms? "))
calval = 0


def calSeries(num):
    for x in range(num):
        calval = int(math.pow(x, 2))*int(math.factorial(abs(x-1)))
        print(calval)

calSeries(num)
