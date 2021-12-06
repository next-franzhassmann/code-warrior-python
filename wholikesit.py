
def likes(names):
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

print(likes(['Max', 'John', 'Mark']))