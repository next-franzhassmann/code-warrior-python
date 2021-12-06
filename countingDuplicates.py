def duplicate_count(text):
    # Write a function that will return the count of distinct
    # case-insensitive alphabetic characters and numeric digits 
    # that occur more than once in the input string. 
    # The input string can be assumed to contain only alphabets 
    # (both uppercase and lowercase) and numeric digits.
    text_min=convertir_minusculas(text)
    print(text_min)
    contador_list=[]
    for i in range(len(text_min)):
        contador=text_min.count(text_min[i])
        contador_list.append(contador)
    #print(contador_list)
    letras_dict={}
    for j in range(len(text_min)):
        if text_min[j] not in letras_dict.keys():
            letras_dict[text_min[j]]=contador_list[j]
    #print(letras_dict)
    duplicates=0
    for l in letras_dict.keys():
        if letras_dict[l] > 1:
            duplicates+=1
    #print(duplicates)
    return duplicates


def convertir_minusculas (text):
    text_min=[]
    for i in range (len(text)):
        text_min.append(text[i].lower())
    return text_min

print(duplicate_count("abcde"))

        


