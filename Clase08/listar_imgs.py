import os
import sys

def archivos_png(directorio):
    png_list = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name[-3:]=='png':
                png_list.append(name)
    return png_list

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio')
    print(archivos_png(sys.argv[1]))