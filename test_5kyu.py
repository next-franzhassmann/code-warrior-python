import pytest

# Casos de prueba para las katas de Codewars de 5kyu
from cgi import test

# Extract the domain name from a URL
from cw5kyu import domain_name, gap

@pytest.mark.parametrize ("url,response",
                        [("http://github.com/carbonfive/raygun","github"),
                         ("http://www.zombie-bites.com","zombie-bites"),
                         ("https://www.cnet.com","cnet")
                        ])
def test_domain_name(url,response):
    assert domain_name(url) == response

#Moving Zeros To The End
from cw5kyu import move_zeros

def test_move_zeros():
    assert move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]

# Rot13
from cw5kyu import rot13

@pytest.mark.parametrize("texto,response",
                        [("Test","Grfg"),
                         ("test","grfg")
                        ])
def test_rot13(texto,response):
    assert rot13(texto) ==response

#Valid Parentheses
from cw5kyu import valid_parentheses

@pytest.mark.parametrize("lista,res",
                        [("()",True),
                        (")(()))",False),
                        ("(",False),
                        ("(())((()())())",True), 
                        ("()jgpy(()u)r)e((tln)gmd)ghxxbj",False),
                        ("r())qx(n(hyy)a)y)(rnbx)f",False)           
                        ])
def test_valid_parentheses(lista,res):
    assert valid_parentheses(lista) == res

#Gap in Primes
from cw5kyu import gap

@pytest.mark.parametrize("g,m,n,res",
                       [(2,3,50,[3,5]),
                        (4,130,200,[163,167]),
                        (6,100,110,None),
                        (2,100,110,[101, 103]),
                        (4,100,110,[103, 107]),
                        (8,300,400,[359, 367]),
                        (10,300,400,[337, 347]),
                        (2,100,103,[101, 103])
                        ])
def test_gap(g,m,n,res):
    assert gap(g, m, n) == res



