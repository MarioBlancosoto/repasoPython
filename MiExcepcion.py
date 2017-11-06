
class MinhaExcepcion (Exception):
    def __init__(self,valor):
        self.valor = valor

    #Definimos el mensaje que lanzará nuestra excepción
    def __str__(self):
        return "Erro :" +str(self.valor)

n =15

try:
 if n == 15:
  raise MinhaExcepcion("Por que si")

except MinhaExcepcion as e:
        print(e)