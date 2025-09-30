def lee_enteros(n):
    '''
    Lee n enteros desde el teclado y los devuelve en una lista
    '''
    res = []
    for i in range(n):
        numero = int(input("Escriba un número entero " + str(i + 1) + ":" ))
        res.append(numero)
    return res

if __name__ == '__main__':
    cuantos = int(input("Cuantos números quieres leer?:"))
    numeros = lee_enteros(cuantos)
    print(numeros)

    print("Número máximo de la lista", max(numeros))

    if lee_enteros == 0:
            print("No es posible calcular la media")
    else:
         print("Media:", sum(numeros)/len(numeros))


    contador = 0
    for n in numeros:
         if n % 2 == 0:
              contador += 1
    print("Números de enteros pares",contador)

    lista_filtrada = []
    for n in numeros:
        if n > 10:
            lista_filtrada.append(n)
    print("Números mayores de 10:", lista_filtrada)