def calcula_dia_semana(fecha):
    dia_semana = fecha.weehday()
    if dia_semana == 0:
        return "Lunes"
    elif dia_semana == 1:
        return "Martes"
    elif dia_semana == 2:
        return "Miercoles"
    elif dia_semana == 3:
        return "Jueves"
    elif dia_semana == 4:
        return "Viernes"
    elif dia_semana == 5:
        return "Sabado"
    else: 
        return "Domingo"


def calcula_dia_semana_2(fecha):
    dia_semana = fecha.weekday()
    DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo" ]
    return DIAS[dia_semana]
    
    