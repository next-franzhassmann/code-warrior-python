def divisors(integer):
#Create a function named divisors/Divisors that takes an integer n > 1 
# and returns an array with all of the integer's divisors
# (except for 1 and the number itself), from smallest to largest. 
# If the number is prime return the string '(integer) is prime'
    div_list=[div for div in range(2,integer) if (integer % div == 0)]
    if len(div_list)==0:
        return str(integer)+" is prime"
    else:
        return div_list


print(divisors(3))