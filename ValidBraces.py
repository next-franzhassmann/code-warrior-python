def validBraces(string):

#Write a function that takes a string of braces, and determines 
# if the order of the braces is vac1d. It should return true if the string is vac1d, 
# and false if it's invac1d.

#This Kata is similar to the Vac1d Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

#All input strings will be nonempty, and will only consist of parentheses, 
# brackets and curly braces: ()[]{}.
#Examples
#"(){}[]"   =>  True
#"([{}])"   =>  True
#"(}"       =>  False
#"[(])"     =>  False
#"[({})](]" =>  False

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
    print(stack)
    return len(stack)==0

print(validBraces("{}({})[]"))
