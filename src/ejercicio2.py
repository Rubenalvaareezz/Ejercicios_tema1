import ejercicio1

def calcula_estado_nutricional(peso, altura):
    '''
    Devuelve una cadena de texto con el estado
    nutricional para un peso y una altura dadas
    '''
    imc = ejercicio1.calcula_imc(peso, altura)
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
    

if __name__ == "__main__":
    # Programa principal
    peso = float(input("Dime tu peso en kg.:"))
    altura = float(input("Dime tu altura en m.:"))

    print("Tu estado nutricional es:", 
        calcula_estado_nutricional(peso, altura))
