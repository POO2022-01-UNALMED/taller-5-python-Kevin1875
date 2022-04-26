from zooAnimales.animal import Animal

class Anfibio(Animal):
  listado=[]
  ranas=0
  salamandras=0
  def __init__(self, nombre,edad,habitat, genero, colorPiel,venenoso):
    Animal.__init__(self, nombre,edad,habitat, genero)
    self.colorPiel=colorPiel
    self.venenoso=venenoso
    Anfibio.listado.append(self)

  def movimiento(self):
    return("saltar")
  @classmethod
  def crearRana(cls, nombre, edad, genero):
    rana=Anfibio(nombre, edad, "selva", genero, "rojo", False)
    Anfibio.ranas+=1
    return rana
  @classmethod
  def crearSalamandra(cls, nombre, edad, genero):
    salamandra=Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    Anfibio.salamandras+=1
    return salamandra
  @classmethod
  def cantidadAnfibios(cls):
    return (len(Anfibio.listado))


  def getColorPiel(self):
    return self.colorPiel

  def getNombre(self):
    return self.nombre
  
  def isVenenoso(self):
    return self.venenoso

  @classmethod
  def getListado(cls):
    return cls._listado
    
    
    
    
  
  
  