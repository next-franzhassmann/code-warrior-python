def alphabet_position(text):
#given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
    text_filtered=[]
    for i in range(len(text)):
        letra=text[i].lower()
    #print(ord('a')) -- 97
    #print(ord('z')) -- 122
        if ord(letra)>=97 and ord(letra)<=122:
            text_filtered.append(ord(letra)-96)
    result=""
    for i in range(len(text_filtered)):
        result=result+str(text_filtered[i])
        if i<len(text_filtered)-1:
            result=result+" "

    return result

print(alphabet_position("The sunset sets at twelve o' clock."))
