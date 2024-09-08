def crear_matriz(n): 
    return [[j + i*n for j in range(1, n+1)] for i in range(n)] 
if __name__ == '__main__': 
    n = 3 
    matriz = crear_matriz(n) 
    for fila in matriz: 
        print(fila)