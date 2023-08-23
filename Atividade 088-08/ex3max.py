

def maximo(lista: list[int]) -> int:
    ''''''
    maximo = max(lista)
    return maximo

def maximo2(lista: list[int]) -> int:
    ''''''
    assert lista != [], 'Erro: a lista necessita de ao menos um elemento.'
    aux = lista[0]

    for num in lista:
        if num > aux:
            aux = num
    return aux


lista = [-100,-400,-10,-1000]

print(maximo(lista))

print(maximo2(lista))

def crescente(lista: list[int]) -> list:
    ''''''
    aux = []

    for lista in range(len(lista)):
        max =  maximo(lista)


    return aux

print(crescente(lista))