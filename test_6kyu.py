# Casos de prueba para las katas de Codewars de 6kyu
from cgi import test

# Duplicate counts
from cw6kyu import duplicate_count

def test_duplicate_count_1():
    assert duplicate_count('abcde') == 0
def test_duplicate_count_2():   
    assert duplicate_count('aabbcde') == 2
def test_duplicate_count_3():
    assert duplicate_count('aabBcde') == 2
def test_duplicate_count_4():
    assert duplicate_count('indivisibility') == 1
def test_duplicate_count_5():
    assert duplicate_count('Indivisibilities') == 2
def test_duplicate_count_6():
    assert duplicate_count('aA11') == 2
def test_duplicate_count_7():
    assert duplicate_count('ABBA') == 2

#Who likes it?
from cw6kyu import likes

def test_likes_1():
    assert likes([]) == "no one likes this"
def test_likes_2():
    assert likes(["Peter"]) == "Peter likes this"   
def test_likes_3():
    assert likes(["Jacob", "Alex"]) == "Jacob and Alex like this"  
def test_likes_4():
    assert likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
def test_likes_5():
    assert likes(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this"   

#Replace With Alphabet Position
from cw6kyu import alphabet_position

def test_alphabet_position1_():
    assert alphabet_position("The sunset sets at twelve o' clock.") \
        == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

#Does my number look big in this?
from cw6kyu import narcissistic

def test_narcissistic_1():
    assert narcissistic(153)==True
def test_narcissistic_2():
    assert narcissistic(1938)==False

#Delete occurrences of an element if it occurs more than n times
from cw6kyu import delete_nth

def test_delete_nth_1():
    assert delete_nth([1,1,1,1],2)==[1,1]
def test_delete_nth_2():
    assert delete_nth([20,37,20,21],1)==[20,37,21]
def test_delete_nth_3():
    assert delete_nth([1,2,3,1,2,1,2,3],2)==[1,2,3,1,2,3]

#Valid braces
from cw6kyu import validBraces

def test_validbraces_1():
    assert validBraces("(){}[]") == True
def test_validbraces_2():
    assert validBraces("([{}])") == True
def test_validbraces_3():
    assert validBraces("(}") == False
def test_validbraces_4():
    assert validBraces("[(])") == False  
def test_validbraces_5():
    assert validBraces("[({})](]") == False
    
#Playing with digits
from cw6kyu import dig_pow

"""
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""

def test_digpow_1():
    assert dig_pow(89,1)==1
def test_digpow_2():
    assert dig_pow(92,1)==-1
def test_digpow_3():
    assert dig_pow(695,2)==2
def test_digpow_4():
    assert dig_pow(46288,3)==51

##Highest Scoring Word
from cw6kyu import high

def test_high():
    assert high('what time are we climbing up the volcano')=="volcano"

#Find the unique number
from cw6kyu import find_uniq

def test_find_uniq_1():
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
def test_find_uniq_2():
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55


