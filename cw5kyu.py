from __future__ import division
import re

def domain_name(url):
    """ Write a function that when given a URL as a string, 
    parses out just the domain name and returns it as a string.
    domain_name("http://github.com/carbonfive/raygun") == "github" 
    domain_name("http://www.zombie-bites.com") == "zombie-bites"
    domain_name("https://www.cnet.com") == "cnet"
    """
    patron='(https*://)?(www.)?([\w-]+.)'
    name=re.findall(patron,url)
    _,_,res = (name[0])
    domain=res.split('.')
    return domain[0]

# Moving Zeros To The End   
    
def move_zeros(array):
    """Write an algorithm that takes an array and moves all of the zeros to the end, 
    preserving the order of the other elements.
    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
    """
    aux_nz=[]
    aux_z=[]
    for e in array:
        if e == 0:
            aux_z.append(e)
        else:
            aux_nz.append(e)
    return (aux_nz+aux_z)

# Rot13
def rot13(message):
    """ROT13 is a simple letter substitution cipher that replaces a letter with the letter 
    13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
    
    Create a function that takes a string and returns the string ciphered with Rot13. 
    If there are numbers or special characters included in the string, they should be 
    returned as they are. Only letters from the latin/english alphabet should be shifted, 
    like in the original Rot13 "implementation".
    rot13("Test") -> "Grfg"
    rot13("test") -> "grfg """

    # Construimos encoder
    alfa_str='abcdefghijklmnopqrstuvwxyz'
    alfa13_str='nopqrstuvwxyzabcdefghijklm'
    alfa_encoder={}
    for i in range(0,len(alfa13_str)):
        alfa_encoder[alfa_str[i]]=alfa13_str[i]
    #Procesamos mensaje
    l_res=[]
    for c in message:
        if 97 <= ord(c) <= 122: # caracter en minúlculas
            l_res.append(alfa_encoder[c])
        elif 65 <= ord(c) <= 90: # caracter en mayúsculas
            l_res.append(alfa_encoder[c.lower()].upper())
        else:   # cuaqluier otra cosa no lo codificamos
            l_res.append(c)
    return ''.join(l_res)

#Valid Parentheses
def valid_parentheses(string):
    """Write a function that takes a string of parentheses, and determines if the order of 
    the parentheses is valid.
    The function should return true if the string is valid, and false if it's invalid.
    Constraints
    0 <= input.length <= 100
    Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII 
    characters. Furthermore, the input string may be empty and/or not contain any 
    parentheses at all. Do not treat other forms of brackets as 
    parentheses (e.g. [], {}, <>).
    """
    l_parentesis=[]
    for s in string:
        if s == '(' or s == ')':
            l_parentesis.append(s)
    stack=[] # Usamos una lista como una pila fifo. Con el último elemento como head
    for p in l_parentesis:
        if p == '(': # abre parentesis -> metemos '(' abierto en pila
            stack.append(p)
        elif p == ')':
            try:
                stack.pop() # cierra parentesis -> sacamos parentesis abierto de pila
            except (IndexError): # cuando mas parentesisi cerrados que abiertos
                return False
    #Si están todos los parentesis cerrados la pila debe ser vacía
    return len(stack) == 0

#Gap in Primes
def es_primo(n):
    """Devuelve si un numero es primo"""
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def lista_primos(n,m):
    """Devuelve lista primos entre n y m"""
    primos=[p for p in range(n,m+1) if es_primo(p)]
    return primos

def gap2(g, m, n):
    primos=lista_primos(m,n)
    gaps=[]
    for i in range(0,len(primos)-1):
        gap=primos[i+1]-primos[i]
        gaps.append(gap)
    gaps.append(-1) #gap del ultimo primo no existe (-1)
    lista_gaps=list(zip(primos,gaps))
    res=[(primo,gap) for primo,gap in lista_gaps if gap==g]
    if len(res)==0:
        return None
    else:
        sol_p,sol_gap=res[0] #Devolvemos siempre el primero
        resultado=list((sol_p,sol_p+sol_gap))
        return resultado

def gap(g, m, n):
    """ The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. 
    From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the 
    following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43
    A prime gap of length n is a run of n-1 consecutive composite numbers between two 
    successive primes
    this function should return the first pair of two prime numbers spaced with a gap 
    of g between the limits m, n if these numbers exist otherwise None.
        g (integer >= 2) which indicates the gap we are looking for
        m (integer > 2) which gives the start of the search (m inclusive)
        n (integer >= m) which gives the end of the search (n inclusive)
        n won't go beyond 1100000.
    """
    for p in range(m,n+1):
        if es_primo(p):
            i=1
            while not es_primo(p+i):
                i+=1
            p_sucesivo=p+i
            if p_sucesivo-p==g:
                return list((p,p_sucesivo))
    return None
