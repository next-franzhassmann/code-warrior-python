# Casos de prueba para las katas de Codewars de 5kyu
from cgi import test

# Extract the domain name from a URL
from cw5kyu import domain_name

def test_domain_name_1():
    assert domain_name("http://github.com/carbonfive/raygun") == "github"
def test_domain_name_2():
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
def test_domain_name_3():
    assert domain_name("https://www.cnet.com") == "cnet"

#Moving Zeros To The End
from cw5kyu import move_zeros

def test_move_zeros():
    assert move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]

# Rot13
from cw5kyu import rot13

def test_rot13_1():
    assert rot13("Test") =="Grfg"
def test_rot13_3():
    assert rot13("test") =="grfg"   



