import os
import datetime
import listar_imgs

def ordenar_imgs(directorio, nuevo_directorio):
    os.mkdir(nuevo_directorio)
    img_list = listar_imgs.archivos_png(directorio)
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name in img_list:
                nombre, fecha = procesar_nombre(name)
                os.rename(os.path.join(root,name),os.path.join(nuevo_directorio,nombre))
    for root, dirs, files in os.walk(directorio):
        if not dirs and not files:
            os.rmdir(root)
        #print(root, dirs, files)
            
def procesar_nombre(fname):
    nombre_corregido = fname[:-13] + '.png'
    fecha = datetime.datetime.strptime(fname[-12:-4], '%Y%m%d')
    return nombre_corregido, fecha

ordenar_imgs('../Data/ordenar','../Data/ordenar/imgs_procesadas')