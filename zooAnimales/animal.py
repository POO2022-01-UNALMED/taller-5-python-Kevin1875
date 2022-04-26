from classroom.zona import Zona
from classroom.zoologico import Zoologico

class Animal:
  totalAnimales=0
  def __init__(self, nombre,edad,habitat, genero):
    self.nombre=nombre
    self.edad=edad
    self.habitat=habitat
    self.genero=genero
    self.zona = None
    Animal.totalAnimales+=1

  def toString(self):
    if self.zona != None:
      return "Mi nombre es " + self.nombre + ", tengo una edad de " + str(self.edad) + ", habito en " + self.habitat + " y mi genero es " + self.genero + ", la zona en la que me ubico es " + self.zona.getNombre() + ", en el " + self.zona.getZoo().getNombre()
    else:
      return "Mi nombre es " + self.nombre + ", tengo una edad de " + str(self.edad) + ", habito en " + self.habitat + " y mi genero es " + self.genero
  
  def movimiento(self):
    return("desplazarse")

  def getNombre(self):
    return self.nombre

  def getEdad(self):
    return self.edad

  def getHabitat(self):
    return self.habitat

  def getGenero(self):
    return self.genero

  @classmethod
  def totalPorTipo(cls):
    from zooAnimales.mamifero import Mamifero
    from zooAnimales.ave import Ave
    from zooAnimales.reptil import Reptil
    from zooAnimales.pez import Pez
    from zooAnimales.anfibio import Anfibio

    return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\nAves : " + str(Ave.cantidadAves()) + "\nReptiles : " + str(Reptil.cantidadReptiles()) + "\nPeces : " + str(Pez.cantidadPeces()) + "\nAnfibios : " + str(Anfibio.cantidadAnfibios())
    
  
  @classmethod
  def getTotalAnimales(cls):
    return cls.totalAnimales

  