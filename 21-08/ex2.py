def digitos(n: int) -> int:
    '''
    Recebe um número N e devolve quantos dígitos ele possui, sem converter para str.

    Exemplo:

    >>> digitos(10)
    2
    
    >>> digitos(333)
    3

    >>> digitos(15000)
    5

    '''
    numero = 10

    while (n / numero) != 1:
        pass


print(digitos(110))
