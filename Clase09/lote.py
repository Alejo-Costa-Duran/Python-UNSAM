import fileparse

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def costo(self):
        return self.cajones*self.precio
    
    def vender(self, num_cajon):
        self.cajones -= num_cajon

    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'


if __name__ == '__main__':
    with open('../Data/camion.csv') as lineas:
        camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
