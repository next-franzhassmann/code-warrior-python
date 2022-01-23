#Sudoku Solution Validator

def devuelve_subloques_nxn_de_board(board,n):
    """Devuelve una lista de subloques nxn de un tablero"""
    bloques_board=[]
    for bloque_filas in range(0,len(board),n):
        res_bloque=devuelve_subloques_nxn_en_fila(board,bloque_filas,3)
        bloques_board += res_bloque
    return bloques_board

def devuelve_subloques_nxn_en_fila(board,f, n):
    """ Dado un tablero, devuelve sus subtableros nxn en la fila f"""
    lista_subloques=[]
    for col_idx in range (0,len(board),n):
        l_subfilas=[]
        for fila_idx in range (f,f+n,1):
            subfila=board[fila_idx][col_idx:col_idx+n]
            l_subfilas.append(subfila)
        lista_subloques.append(l_subfilas)
    return lista_subloques

def devuelve_columnas(board):
    """ Dado un tablero, devuelve su lista de columnas"""
    lista_columnas=[]
    for y in range (0,len(board)):
        una_columna=[]
        for f in  board:
            una_columna.append(f[y])
        lista_columnas.append(una_columna)
    return lista_columnas

def valid_solution(board):
    """Write a function that accepts a 2D array representing a Sudoku board, and returns 
    true if it is a valid solution, or false otherwise. The cells of the sudoku board 
    may also contain 0's, which will represent empty cells. Boards containing one or 
    more zeroes are considered to be invalid solutions.

    The board is always 9 cells by 9 cells, and every cell only contains integers 
    from 0 to 9
    """
    #board es  9x9: [filas] de [columnas] como elemnto
    #Construimos listas de filas y columnas 
    lista_filas= board
    #lista_filas_y_columnas(board,0,9)
    # Comprobamos condicionnes sudoku
    res=True
    #Comprobamos si tiene 0s
    for f in lista_filas:
        if not res: break
        if res and f.count(0) > 0:
            res = False
    #Sudoku válido: Todas las filas deben contener todos los valores de 1 a 9
    for n in range (1,10):
        if not res: break
        for f in lista_filas:
            if res and f.count(n) > 1:
                res = False
                break
    #Sudoku válido: Todas las columnas deben contener todos los valores de 1 a 9
    lista_columnas=devuelve_columnas(board)
    for n in range (1,10):
        if not res: break
        for c in lista_columnas:
            if res and c.count(n) > 1:
                res=False
                break
    #ojo, todos los subloques de 3x3 deben contener los numeros de 1 a 9
    #construye subloques
    if res:
        for sub_bloque in (devuelve_subloques_nxn_de_board(board,3)):
            lista_nums_bloque=[]
            for sub_fila in sub_bloque:
                for num in sub_fila:
                    lista_nums_bloque.append(num)
            num_dist_bloque=set(lista_nums_bloque)
            if len(num_dist_bloque) < 9:
                res = False
    return res


