

class Zoologico:

    def __init__(self, nombre, ubicacion):
      self.nombre=nombre
      self.ubicacion=ubicacion
      self.zonas=[]

    def agregarZonas(self, zonas):
      self.zonas.append(zonas)

    def cantidadTotalAnimales(self):
      a=0
      for i in self.zonas:
        a+=len(i.animales)
      return (a)

    def getZona(self):
      return self.zonas
    def getNombre(self):
      return self.nombre
