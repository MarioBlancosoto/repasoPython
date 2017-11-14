

def nome_Funcion (parametro1,parametro2="Hola"):
    """Esta función exemplifica a definición da declaración de funcións"""
    print(parametro1)
    print(parametro2)

nome_Funcion(20,"Mensaxe de acollida")
#reasignación de variables dentro de la misma función
nome_Funcion(parametro2="Mensaxe",parametro1=3)

nome_Funcion(2,3)

nome_Funcion(1000)

#Muestra de función con asignacion de varios valores
def punto (x=0,y=500):
    print(x)
    print(y)

punto(2,3)
punto(1)
punto()
punto(y=3)

def funcion2 (param1,*varios):
    print(param1)
    for elemento in varios:
      print(elemento)
print("---------")
funcion2(1)
funcion2(1,2)

#funcion en la que recogemos con dos asteriscos varios parametros y despues los recorremos con .items()
def funcion3(parametro,**variables):
    print(parametro)
    for valor in variables.items():
        print(valor)

funcion3("--------",dous=2,tres=3,catro=4)


def funcion4(a,b):
    a=a+1
    b.append(23)
    print(a,b)
#en el primer print valdría 6 dado el a=a+1,entonces sería 6 y el b.append que en este caso añadiria 23 al 4 con paréntesis, [4,23]
z=5
x=[4]
funcion4(z,x)
print(z,x)


"""Aquí retornamos x*2 e y*2 para despúes asignarle ese valor a a,b inicializando los valores de la función en 1 y 4 para después sacar por 
pantalla 2 y 8"""
def doblaPunto (x,y):
    return x*2,y*2

a,b=doblaPunto(1,4)

print(a,b)



"""Excepcións """

