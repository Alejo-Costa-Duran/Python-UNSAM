class Canguro:
    def __init__(self, nombre, contenido = None):
        self.nombre = nombre
        if not contenido:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido
        
    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(objeto)
    
    def __str__(self):
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

#class Canguro:
#    """Un Canguro es un marsupial."""
#    
#    def __init__(self, nombre, contenido=None):
#       """Inicializar los contenidos del marsupio.
#
#        nombre: string
#        contenido: contenido inicial del marsupio, lista.
#        """
#        self.nombre = nombre
#        if not contenido:
#            self.contenido_marsupio = []
#        else:
#            self.contenido_marsupio = contenido
#        
#    def __str__(self):
#        """devuelve una representación como cadena de este Canguro.
#        """
#        t = [ self.nombre + ' tiene en su marsupio:' ]
#        for obj in self.contenido_marsupio:
#            s = '    ' + object.__str__(obj)
#            t.append(s)
#        return '\n'.join(t)

#    def meter_en_marsupio(self, item):
#        """Agrega un nuevo item al marsupio.
#
#        item: objecto a ser agregado
#        """
#        self.contenido_marsupio.append(item)

#
#madre_canguro = Canguro('Madre')
#cangurito = Canguro('gurito')
#madre_canguro.meter_en_marsupio('billetera')
#madre_canguro.meter_en_marsupio('llaves del auto')
#madre_canguro.meter_en_marsupio(cangurito)
#
#print(madre_canguro)
#print(cangurito)