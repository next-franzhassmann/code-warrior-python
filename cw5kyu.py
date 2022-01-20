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

