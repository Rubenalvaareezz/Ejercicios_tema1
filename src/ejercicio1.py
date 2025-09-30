def calcula_imc(peso, altura):
    '''
    Calcula el índice de masa corporal
    ''' 
    return peso / (altura ** 2)

if __name__ == '__main__':
    peso = float(input("Dime tu peso en kg.:"))
    altura = float(input("Dime tu altura en m.:"))

    imc = calcula_imc(peso, altura)
    print("Tu imc es", imc)