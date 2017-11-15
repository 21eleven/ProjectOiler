"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
import sys
limit = 10000 

n = 2

while n < limit:
    pan = str(n * 1)
    for i in range(2,20):
        pan=pan+str(n*i)
        if len(str(pan)) >= 9:
            break
    if len(pan) == 9:
        if "1" in pan and "2" in pan and "3" in pan and "4" in pan and "5" in pan and "6" in pan and "7" in pan and "8" in pan and "9" in pan:
            print(n, pan)
    n+=1


