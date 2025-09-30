import ejercicio1, ejercicio2

def imprime_estados_nutricionales(personas):
    '''
    Recibe una lista de tuplas, siendo
    cada tupla el peso y la altura de una persona,
    y muestra para cada una un mensaje con el imc
    y el estado nutricional
    EJ. de valor para personas:
        personas = [
                (60.0, 1.6),
                (75.4, 1.75),
                (87.9, 1.69),
                (45.1, 1.65)
            ]
    '''
    for p in personas: # tambien se puede: for peso, altura in personas
        peso = p[0]
        altura = p[1]
        imc = ejercicio1.calcula_imc(peso, altura)
        estado_nutricional = ejercicio2.calcula_estado_nutricional(
                                                    peso, altura)
        # TODO: hacer un print mostrando la informacion
