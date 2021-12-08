def dig_pow(n, p):

#Given a positive integer n written as abcd... (a, b, c, d... being digits) and a 
# positive integer p

#we want to find a positive integer k, if it exists, such as the sum of the digits 
# of n taken to the successive powers of p is equal to k * n.
#In other words:

#Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

#If it is the case we will return k, if not return -1.

#ex dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
    
    num_str=str(n)
    acc=0
    exp=p
    for dig in num_str:
        acc+=int(dig)**exp
        exp+=1
    if acc % n == 0:
        k=int(acc/n)
        return k
    else:
        return -1

print(dig_pow(46288, 3))