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