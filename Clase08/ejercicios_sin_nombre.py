#%% Ej: 8.2

import datetime
 
def primavera_cronica():
    '''
    Devuelve los días que faltan para la primavera desde el instante
    actual.
    '''
    hoy = datetime.date.today()
    año_actual = hoy.year
    inicio_prim = datetime.date(año_actual,9,21)
    final_prim = datetime.date(año_actual,12,21)
    dias_primavera = (final_prim-inicio_prim).days
    dias = (inicio_prim-hoy).days
    if dias>0:
        return dias
    elif dias>-dias_primavera:
        return '¡Estamos en primavera!'
    else:
        sig_primavera = datetime.date(año_actual+1,9,21)
        dias = (sig_primavera-hoy).days
        return dias

#%% Ej 8.3

def fecha_reincorporacion(start_date, licencia):
    date_1 = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    end_date = date_1 + datetime.timedelta(days=licencia)
    return end_date

#%% Ej 8.4

def dias_habiles(inicio, fin, feriados):
    init_date = datetime.datetime.strptime(inicio, "%d/%m/%Y")
    end_date = datetime.datetime.strptime(fin, "%d/%m/%Y")
    feriados_ls = [datetime.datetime.strptime(feriado, "%d/%m/%Y") for feriado in feriados]
    amount_days = (end_date-init_date).days    
    finde = (5,6)
    dias_laborables = [ datetime.datetime.strftime(y, "%d/%m/%Y") for x in range(amount_days+1)
                       if ((y:= init_date+datetime.timedelta(x)) not in feriados_ls) and (y.weekday() not in finde)]
    return dias_laborables

#%% Ej 8.5
import os

def archivos_png(directorio):
    png_list = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name[-3:]=='png':
                png_list.append(name)
    return png_list

a = archivos_png('../Data/ordenar')

#%%

import os
import datetime
import time

camino = '../Clase06/rebotes.py'

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))
#%%Ejemplo arbolado veredas

import pandas as pd
import os
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel].copy()
ejemplares = df['nombre_cientifico'].value_counts()
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
#df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')