from zooAnimales.animal import Animal

class Reptil(Animal):
  listado=[]
  iguanas=0
  serpientes=0
  def __init__(self, nombre,edad,habitat, genero, colorEscamas,largoCola):
    Animal.__init__(self, nombre,edad,habitat, genero)
    self.colorEscamas=colorEscamas
    self.largoCola=largoCola
    Reptil.listado.append(self)

  def movimiento(self):
    return("reptar")
  @classmethod
  def crearIguana(cls, nombre, edad, genero):
    rana=Reptil(nombre, edad, "humedal", genero, "verde", 3)
    Reptil.iguanas+=1
    return rana
  @classmethod
  def crearSerpiente(cls, nombre, edad, genero):
    salamandra=Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    Reptil.serpientes+=1
    return salamandra
  @classmethod
  def cantidadReptiles(cls):
    return (len(Reptil.listado))


  def getColorEscamas(self):
    return self.colorEscamas

  def getNombre(self):
    return self.nombre
  
  def  getLargoCola(self):
    return self.largoCola

  @classmethod
  def getListado(cls):
    return cls._listado
