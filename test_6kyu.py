import pytest

# Casos de prueba para las katas de Codewars de 6kyu
from cgi import test
from urllib import response

# Duplicate counts
from cw6kyu import duplicate_count

@pytest.mark.parametrize("texto,respuesta",
                        [('abcde',0),
                        ('aabbcde',2),
                        ('aabBcde',2),
                        ('indivisibility',1),
                        ('Indivisibilities',2),
                        ('aA11',2),
                        ('ABBA',2)
                        ])
def test_duplicate_count(texto,respuesta):
    assert duplicate_count(texto) == respuesta

#Who likes it?
from cw6kyu import likes


@pytest.mark.parametrize("lista_n,resp",
                        [([],"no one likes this"),
                        (["Peter"],"Peter likes this"),  
                        (["Jacob", "Alex"],"Jacob and Alex like this"),
                        (["Max", "John", "Mark"],"Max, John and Mark like this"), 
                        (["Alex", "Jacob", "Mark", "Max"],"Alex, Jacob and 2 others like this")                  
                        ])
def test_likes(lista_n,resp):
    assert likes(lista_n) == resp  


#Replace With Alphabet Position
from cw6kyu import alphabet_position

def test_alphabet_position1_():
    assert alphabet_position("The sunset sets at twelve o' clock.") \
        == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

#Does my number look big in this?
from cw6kyu import narcissistic

@pytest.mark.parametrize("num,resp",
                        [(153,True),
                        (1938,False)
                        ])
def test_narcissistic(num,resp):
    assert narcissistic(num)==resp

#Delete occurrences of an element if it occurs more than n times
from cw6kyu import delete_nth

@pytest.mark.parametrize("lista,n,resp",
                        [([1,1,1,1],2,[1,1]),
                         ([20,37,20,21],1,[20,37,21]),
                         ([1,2,3,1,2,1,2,3],2,[1,2,3,1,2,3])
                        ])
def test_delete_nth(lista,n,resp):
    assert delete_nth(lista,n)==resp

#Valid braces
from cw6kyu import validBraces

@pytest.mark.parametrize("input,resp",
                        [("(){}[]",True),
                        ("([{}])",True),
                        ("(}",False),
                        ("[(])",False),
                        ("[({})](]",False)
                        ])
def test_validbraces(input,resp):
    assert validBraces(input) == resp
    
#Playing with digits
from cw6kyu import dig_pow

"""
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""
@pytest.mark.parametrize("num,k,resp",
                        [(89,1,1),
                        (92,1,-1),
                        (695,2,2),
                        (46288,3,51)
                        ])
def test_digpow(num,k,resp):
    assert dig_pow(num,k)==resp

##Highest Scoring Word
from cw6kyu import high

def test_high():
    assert high('what time are we climbing up the volcano')=="volcano"

#Find the unique number
from cw6kyu import find_uniq

@pytest.mark.parametrize("lista,resp",
                        [([ 1, 1, 1, 2, 1, 1 ],2),
                        ([ 0, 0, 0.55, 0, 0 ],0.55)
                        ])
def test_find_uniq(lista,resp):
    assert find_uniq(lista) == resp



