'''Nikki has given Mansi a String str of length L.The string str is composed of only lowercase alphabets. She has asked Mansi now to calculate the function F of this string' all substrings of length Z. Nikki has also given Mansi two number K and MOD.

The Function F is calculated in this way.

F= str[0] * k^0 + str[1] * k^1 + str[2] * k^2 + ......str[Z-1] * k^(Z-1).
Take the Ascii Values of Alphabets while computing F. 
'a'- 'z'= 97 to 122.
You need to Print the Maximum F among all the substrings of length Z.
Since F may come out to be very large, You can take its modulo by 1e9+7.

 

Input:
The first Line contains T- denoting the number of test cases.
The first line of each test case contains 3 integers- N(Length of the string), Z(Length of each substring that you need to take), K(used in calculating F)
The second line contains the String - Consisting of lowercase alphabets only.

Output:
Foreachtestcase- Output the maximum F among all the substrings of length Z.

Constraints:
1<=T<=100
1<=N<=1000000
1<=Z<=N
1<=K<=2018

Explanation:
Input:
1
9 6 10
nikitasha

Output:
12597675

Explanation:
F("nikita")= 'n'*10^0 + 'i'*10^1 +'k'*10^2 + 'i'*10^3 +'t'*10^4 + 'a'*10^5 = 10976860
F("ikitas")= 'i'*10^0 + 'k'*10^1 +'i'*10^2 + 't'*10^3 +'a'*10^4 + 's'*10^5 = 12597675
F("kitash")= 'k'*10^0 + 'i'*10^1 +'t'*10^2 + 'a'*10^3 +'s'*10^4 + 'h'*10^5 = 11659757
F("itasha")= 'i'*10^0 + 't'*10^1 +'a'*10^2 + 's'*10^3 +'h'*10^4 + 'a'*10^5 = 10865965


12597675 Being the Maximum*/ '''

import math

testCases = int(input("How many testCases? "))
threeNum = int(input("Enter 3 numbers.. "))
word = int(input("Enter the string.. "))


def chalangeFunction(testCases, threeNum, word):
    for x in range(num):
        calval = int(math.pow(x, 2))*int(math.factorial(abs(x-1)))
        print(calval)


chalangeFunction(testCases, threeNum, word)
