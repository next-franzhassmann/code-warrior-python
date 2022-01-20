
# Duplicate counts
def duplicate_count(text):
    """Write a function that will return the count of distinct
    case-insensitive alphabetic characters and numeric digits 
    that occur more than once in the input string. 
    The input string can be assumed to contain only alphabets 
    (both uppercase and lowercase) and numeric digits."""
    text_min=text.lower()
    dic_cont={}
    for c in text_min:
        if c not in dic_cont:
            dic_cont[c] = 0
        else:
            dic_cont[c] +=1
    num_dups=0
    for num_car in dic_cont.values():
        if num_car !=0:
            num_dups += 1
    return num_dups

#Who likes it?
def likes(names):
    """You probably know the "like" system from Facebook and other pages. 
    People can "like" blog posts, pictures or other items. We want to create the text that 
    should be displayed next to such an item."""
    msg=""
    if len(names)==0:
        msg="no one likes this"
    elif len(names)==1:
        msg=str(names[0])+" likes this"
    elif len (names)==2:
        msg=str(names[0])+" and "+str(names[1])+" like this"
    elif len (names)==3:
        msg=str(names[0])+", "+ str(names[1])+" and "+ str(names[2])+" like this"
    else:
        msg=str(names[0])+", "+ str(names[1])+" and "+ str(len(names)-2)+" others like this"
    return msg

#Replace With Alphabet Position
def alphabet_position(text):
    """given a string, replace every letter with its position in the alphabet.
    If anything in the text isn't a letter, ignore it and don't return it.
    "a" = 1, "b" = 2, etc.
    """
    
    encoder={}
    for cod_ascii in range(ord('a'),ord('z')+1):
        encoder[chr(cod_ascii)]=cod_ascii-ord('a')+1 #ord('a)'= 97
    
    l_result=[]
    text_min=text.lower()
    for c in text_min:
        if ord(c)>=97 and ord(c)<=122:
            l_result.append(str(encoder[c]))
    return ' '.join(l_result)  

