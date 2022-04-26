from zooAnimales.animal import Animal
class Pez(Animal):
  listado=[]
  salmones=0
  bacalaos=0
  def __init__(self, nombre,edad,habitat, genero, colorEscamas,cantidadAletas):
    Animal.__init__(self, nombre,edad,habitat, genero)
    self.colorEscamas=colorEscamas
    self.cantidadAletas=cantidadAletas
    Pez.listado.append(self)

  def movimiento(self):
    return("nadar")

  @classmethod
  def crearSalmon(cls, nombre, edad, genero):
    rana=Pez(nombre, edad, "oceano", genero, "rojo", 6)
    Pez.salmones+=1
    return rana

  @classmethod
  def crearBacalao(cls, nombre, edad, genero):
    salamandra=Pez(nombre, edad, "oceano", genero, "gris", 6)
    Pez.bacalaos+=1
    return salamandra
  @classmethod
  def cantidadPeces(cls):
    return (len(Pez.listado))


  def getColorEscamas(self):
    return self.colorEscamas

  def getNombre(self):
    return self.nombre
  
  def getCantidadAletas(self):
    return self.cantidadAletas

  @classmethod
  def getListado(cls):
    return cls._listado