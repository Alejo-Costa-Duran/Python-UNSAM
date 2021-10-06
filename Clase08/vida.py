import datetime

def vida_en_segundos(fecha_nac):
    '''
    Pre: Toma la fecha de nacimiento en formato 'dd/mm/AAAA'
    Pos: Devuelve los segundos que transcurrieron desde las 0 horas de la
    fecha ingresada hasta el instante actual.
    '''
    cumple = datetime.datetime.strptime(fecha_nac, "%d/%m/%Y")
    now = datetime.datetime.now()
    total = now-cumple
    return total.total_seconds()