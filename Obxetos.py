
class Punto:
    """Clase punto que define as coordenadas dun punto cartesiano"""
    def __init__(self,x,y):
        self.x = x
        self.y = y



    def mostrarX(self):
        print("coordenada x : "+ str(+self.x))



class Circulo (Punto):
   def __init__(self,x,y,r):
        Punto.__init__(self,x,y)
        self.r=r

   def superficie(self,r):
      return 3.14*r**2


#Obxecto tipo Punto creado cos valores dous e 3
p1= Punto(2,3)
p1.mostrarX()

#Declarado obxecto tipo Circulo,herdando propiedades de Punto
c1 = Circulo(3,5,3)

#MostraX Heredado de Punto
c1.mostrarX()

#Facemos print do parametro Y co nome do obxecto seguido dun punto e o nome
print (c1.y)

#Nova clase pra definir a altura
class TerceiraDimension:
  def __init__(self,h):
      self.h = h


  def mostrarH(self):
     print("Altura :"+str( self.h))

#Clase definida cos constructores de circulo e terceira dimension
class Cilindro(Circulo,TerceiraDimension):
    def __init__(self,x,y,r,h):
     Circulo.__init__(self,x,y,r)
     TerceiraDimension.__init__(self,h)
#Definimos os constructores das outras duas clases

    def volume(self):
         return 3.14*self.r**2*self.h
#Definición de método recollendo r e h
#creamos o obxeto tipo cilindro coas variables das outras clases e damoslle valor aos atributos

#Método privado
    def _superficie(self):
        return 2*3.14*self.r**2+2*3.14*self.r*self.h

#Método accesible
    def superficie(self):
        return self._superficie()

#Printamos a función volume co obxeto creado

cil1 = Cilindro(1, 1, 1, 1)
print(cil1.volume())
print(cil1.y)
print(cil1.superficie())
cil1.mostrarH()




