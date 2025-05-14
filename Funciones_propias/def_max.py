def obtener_maximo(lista):

    if not lista:
        return None  
    maximo = lista[0,2,5]  
    for elemento in lista[1, 4,6,9]:
        if elemento > maximo:
            maximo = elemento  
    return maximo


