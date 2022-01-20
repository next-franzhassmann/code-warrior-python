
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

#Does my number look big in this?
def narcissistic( value ):
    """A Narcissistic Number is a positive number which is the sum of its own digits, 
    each raised to the power of the number of digits in a given base. 
    In this Kata, we will restrict ourselves to decimal (base 10)
    For example, take 153 (3 digits), which is narcisstic: 
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    and 1652 (4 digits), which isn't:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
    """

    value_tuple=tuple(str(value))
    exp=len(value_tuple)
    calc=0
    for i in range(len(value_tuple)):
        calc=calc+int(value_tuple[i])**exp
    return calc==value

#Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    """ Given a list lst and a number N, create a new list that contains each number 
    of lst at most N times without reordering. 
    For example if N = 2, and the input is [1,2,3,1,2,1,2,3], 
    you take [1,2,3,1,2], drop the next [1,2] since this would lead 
    to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
    """
    list_number={}
    for i in range(len(order)):
        list_number[order[i]]=order.count(order[i])
    print(list_number)
    acciones=[] #Lista de acciones por elemento 'M'antener y 'B'orrar
    for j in range(-1,-len(order)-1,-1):
        if list_number[order[j]] > max_e:
            acciones.insert(0,'B')
            list_number[order[j]] -= 1
        else:
            acciones.insert(0,'M')
    list_res=[]
    for k in range (len(order)):
        if acciones[k]=='M':
            list_res.append(order[k])
        k +=1
    return list_res

#Valid braces

def validBraces(string):
    """Write a function that takes a string of braces, and determines 
    if the order of the braces is vac1d. It should return true if the string is vac1d, 
    and false if it's invac1d.
    This Kata is similar to the Vac1d Parentheses Kata, but introduces new characters: 
    brackets [], and curly braces {}. Thanks to @arnedag for the idea!
    All input strings will be nonempty, and will only consist of parentheses, 
    brackets and curly braces: ()[]{}.
    """

    def stack_init ():
        return []

    def stack_push (s:list,e):
        s.append(e)
        return s
    
    def stack_pop (s:list):
        if len(s)>=1:
            s.pop()
        else:
            print("Error, la pila ya está vacía")
    
    def stack_top(s:list):
        if len(s)>0:
            return s[-1]
        else:
            print("Error, la pila ya está vacía")

    def cierra_parentesis(s:list):
        c1=stack_top(s)
        stack_pop(s)
        c2=stack_top(s)
        stack_pop(s)
        if (c1==')' and c2=='(') or (c1==']' and c2=='[') or (c1=='}' and c2=='{'):
            pass
        else:
            stack_push(s,c2)
            stack_push(s,c1)
        
    stack=stack_init()
    i=0
    while  i<=len(string)-1:
        stack_push(stack,string[i])
        if len(stack)>=2:
            cierra_parentesis(stack)
        i+=1
    return len(stack)==0

def dig_pow(n, p):
    """Given a positive integer n written as abcd... (a, b, c, d... being digits) and a 
    positive integer p
    we want to find a positive integer k, if it exists, such as the sum of the digits  
    of n taken to the successive powers of p is equal to k * n.
    In other words:
    Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    If it is the case we will return k, if not return -1.
    #ex dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
    """
    
    num_str=str(n)
    acc=0
    exp=p
    for dig in num_str:
        acc+=int(dig)**exp
        exp+=1
    if acc % n == 0:
        k=int(acc/n)
        return k
    else:
        return -1

##Highest Scoring Word
def high(x):
    """Given a string of words, you need to find the highest scoring word.
    Each letter of a word scores points according to its position in the 
    alphabet: a = 1, b = 2, c = 3 etc.
    You need to return the highest scoring word as a string.
    If two words score the same, return the word that appears earliest in the original 
    string. All letters will be lowercase and all inputs will be valid.
    """

    def word_scoring(p):
        acc=0
        for c in p:
            #print(ord('a')) -- 97
            acc += ord(c)-96
        return acc
        
    lista_palabras=x.split()
    lista_scoring=[]
    for p in lista_palabras:
        lista_scoring.append(word_scoring(p))
    i_max=lista_scoring.index(max(lista_scoring))
    return lista_palabras[i_max]

#Find the unique number
def find_uniq(list):
    """ There is an array with some numbers. All numbers are equal except for one. 
    Try to find it!
    It’s guaranteed that array contains at least 3 numbers.
    The tests contain some very huge arrays, so think about performance.
    """
    vals_distintos=set(list)
    dic_contador={}
    for e in vals_distintos:
        dic_contador[e]=list.count(e)
    for k in dic_contador.keys():
        if dic_contador[k] == 1:
            return k
        
    

