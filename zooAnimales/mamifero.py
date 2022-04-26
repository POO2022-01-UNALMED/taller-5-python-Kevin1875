from zooAnimales.animal import Animal
class Mamifero(Animal):
  listado=[]
  caballos=0
  leones=0
  def __init__(self, nombre,edad,habitat, genero, pelaje,patas):
    Animal.__init__(self, nombre,edad,habitat, genero)
    self.pelaje=pelaje
    self.patas=patas
    Mamifero.listado.append(self)

  
  @classmethod
  def crearCaballo(cls, nombre, edad, genero):
    rana=Mamifero(nombre, edad, "pradera", genero, True, 4)
    Mamifero.caballos+=1
    return rana
    
  @classmethod
  def crearLeon(cls, nombre, edad, genero):
    salamandra=Mamifero(nombre, edad, "selva", genero, True, 4)
    Mamifero.leones+=1
    return salamandra
    
  @classmethod
  def cantidadMamiferos(cls):
    return (len(Mamifero.listado))


  def getCaballos(self):
    return Mamifero.caballos

  def getNombre(self):
    return self.nombre
  
  def isPelaje(self):
    return self.pelaje
  
  def getPatas(self):
    return self.patas

  @classmethod
  def getListado(cls):
    return cls._listado