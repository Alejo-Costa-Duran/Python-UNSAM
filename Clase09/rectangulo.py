class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'


class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 =exit punto2

    def __str__(self):
        return f'({self.punto1}, {self.punto2})'

    def __repr__(self):
        return f'Rectangulo({self.punto1}, {self.punto2})'

    def base(self):
        return abs(self.punto1.x-self.punto2.x)

    def altura(self):
        return abs(self.punto1.y-self.punto2.y)
    
    def area(self):
        return self.base()*self.altura()
    
    def desplazar(self, desplazamiento):
        self.punto1 = self.punto1 + desplazamiento
        self.punto2 = self.punto2 + desplazamiento

    def rotar(self):
        lower_right = Punto(max(punto1.x,punto2.x),min(punto1.y,punto2.y))
        self.punto1 = lower_right
        self.punto2 = lower_right + Punto(self.altura(),self.base())