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

move_zeros([1, 0, 1, 2, 0, 1, 3])