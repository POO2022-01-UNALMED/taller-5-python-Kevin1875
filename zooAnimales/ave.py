from zooAnimales.animal import Animal

class Ave(Animal):
  listado=[]
  halcones=0
  aguilas=0
  def __init__(self, nombre,edad,habitat, genero, colorPlumas):
    Animal.__init__(self, nombre,edad,habitat, genero)
    self.colorPlumas=colorPlumas
    
    Ave.listado.append(self)

  def movimiento(self):
    return("volar")
  @classmethod
  def crearHalcon(cls, nombre, edad, genero):
    rana=Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    Ave.halcones+=1
    return rana
  @classmethod
  def crearAguila(cls, nombre, edad, genero):
    salamandra=Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    Ave.aguilas+=1
    return salamandra
  @classmethod
  def cantidadAves(cls):
    return (len(Ave.listado))


  def getColorPlumas(self):
    return self.colorPlumas

  def getNombre(self):
    return self.nombre
  @classmethod
  def getListado(cls):
    return cls._listado
  
  
  
  
