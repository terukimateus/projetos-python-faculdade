def fibonacci(n: int) -> int:
    ''''''

    lista = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for n in range(n+1):
            if n != 0 and n!=1:
                lista.append(n)  
    
    for num in lista:
        print(lista[num])

print(fibonacci(8))