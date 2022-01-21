import pytest

# Casos de prueba para las katas de Codewars de 5kyu
from cgi import test

# Extract the domain name from a URL
from cw5kyu import domain_name

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





