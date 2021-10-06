import os
import pandas as pd

def f_principal():
    #Defino los nombres de archivos y directorios
    directorio = '../Data'
    archivo_parques = 'arbolado-en-espacios-verdes.csv'
    archivo_vereda = 'arbolado-publico-lineal-2017-2018.csv'
    fname_parques = os.path.join(directorio,archivo_parques)
    fname_vereda = os.path.join(directorio,archivo_vereda)
    ##
    
    #Creo los data frames para cada archivo
    df_parques = pd.read_csv(fname_parques)
    df_veredas = pd.read_csv(fname_vereda)
    
    #Columnas a seleccionar
    cols_parques = ['altura_tot', 'diametro']
    cols_veredas = ['altura_arbol', 'diametro_altura_pecho']
    
    #Defino los data frames de las especies que me interesan
    df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_parques].copy()
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu' ][cols_veredas].copy()
    
    #Renombro las columnas
    df_tipas_veredas.rename(columns={"altura_arbol":"altura_tot", "diametro_altura_pecho":"diametro"}, inplace=True)
    
    #Agrego los ambientes y los concateno
    df_tipas_parques['ambiente'] = 'parque'
    df_tipas_veredas['ambiente'] = 'vereda'
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    
    #Graficos boxplot
    df_tipas.boxplot('diametro',by = 'ambiente')
    df_tipas.boxplot('altura_tot',by = 'ambiente')