#Funcións de orde superior

def saudar(lingua):
    def saudar_es():
        print(" Hola ")

    def saudar_gl():
        print(" Ola ")
    def saudar_en():
        print(" Hello ")
    def saudar_it():
        print("Ciao")

    lingua_funcion = {"es": saudar_gl,
                      "gl": saudar_es,
                      "en": saudar_en,
                      "it": saudar_it}
#A traves de lingua_funcion devolvemos una ristra de funciones,y luego con [lingua] le decimos en la llamada que función queremos de la ristra
    return lingua_funcion[lingua]


funcion = saudar("es")
#print(funcion)

#Declaramos una funcion que realiza el cuadrado de un numero dado
def cadrado(n):
    return n**2

#lista de numeros
l = [1,2,3,4]

#metemos en una variable el mapeado de la lista,y le aplicamos la función del cuadrado a la lista
l2 = list(map(cadrado,l))
#hacemos print de la variable
print(l2)
#Aplicamos a l3 la lista mapeada y le aplicamos la funcion de saudar a es en it y gl,con un for recorremos l3,y ejecutamos la funcion(indice)
l3 = list(map(saudar,["es","en","it","gl"]))

for funcion in l3:
    funcion()


def e_par(n):
    return(n % 2 ==0)
#Aplicamos filter,a la función epar sobre la lista de numeros L
l4 = list(filter(e_par,l))
print(l4)

#Compresión de listas
#Aplicamos la operación sin llamar a la función a L la lista de números con el for
l5 =[n**2 for n in l]
print(l5)
#Aplicamos la operación con la llamada a la función cadrado,y se la aplicamos a l
l6 = [cadrado(n) for n in l]
print(l6)
#por cada  numero en l si es par lo guarda en l7
l7 =[numero for numero in l if numero%2 ==0]
#o
# for n in l:
 #if n%2==0:
 #l4.append(n)
print(l7)

#si x es mayor a 0 multiplicalos por y,en este caso recorriendo los indices i y j
x =[0,1,2,3,4,5]
y=["a","b","c"]
z =[i*j for i in y
        for j in x
        if j>0]
print(z)

#Creamos una lista nueva y le hacemos el cuadrado con el for a la lista l de números,posteriormente recorremos la lista para poder imprimirla
l8 =(n**2 for n in l)
for i in l8:
 print(i)
#Recorremos con un for la función de (numero**2 for numero in l(Recorremos haciendo a cada numero de l su cuadrado)) finalizamos imprimiendo el indice i
for i in (n**2 for n in l):
    print(i)
#Funcion que recibe 3 números,mientras n sea menor a m devuelve n,posteriormente a n le suma el valor de s
def meu_xerador(n,m,s):
    while(n<=m):
        yield n,m,s
        n+=s
#Recorre la función de meu_xerador en un rango de 5 a 15 de 2 en 2,posteriormente imprimimos el índice.
print(meu_xerador(5,15,2))
for i in meu_xerador(5,15,2):
    print(i)

