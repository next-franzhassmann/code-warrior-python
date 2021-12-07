
def narcissistic( value ):
#A Narcissistic Number is a positive number which is the sum of its own digits, 
# each raised to the power of the number of digits in a given base. 
# In this Kata, we will restrict ourselves to decimal (base 10)

    value_tuple=tuple(str(value))
    exp=len(value_tuple)
    calc=0
    for i in range(len(value_tuple)):
        calc=calc+int(value_tuple[i])**exp
    return calc==value


print(narcissistic(153))