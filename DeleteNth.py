def delete_nth(order,max_e):
    # Given a list lst and a number N, create a new list that contains each number 
    # of lst at most N times without reordering. 
    # For example if N = 2, and the input is [1,2,3,1,2,1,2,3], 
    # you take [1,2,3,1,2], drop the next [1,2] since this would lead 
    # to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

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


print(delete_nth([1,2,3,1,2,1,2,3],2))
