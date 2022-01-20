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

rot13("Test")

