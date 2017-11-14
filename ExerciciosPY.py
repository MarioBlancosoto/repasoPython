"""Diccionarios"""


diccionario = {6122:"Miguel",6145:"Adrian",6158:"Silva"}

print (diccionario[6145])
#Esto nos comprueba si está o no está en el diccionario y nos resuelve el problema sin romper el programa
print (diccionario.get(6122,"Clave non atopada"))
# print(diccionario[6322]) con esto nos partiría el programa
#Otra forma para que nos diga si contiene o no el objeto y nos devuelva true o false
print (diccionario.__contains__(6145))
#Con .items devolvenos unha lista de items.
print(diccionario.items())
#Acceder a todalas claves do diccionario
print(diccionario.keys())
#Acceder aos valores do diccionario
print(diccionario.values())
#for pra recorrer todas as claves coa variable valor e despóis recollemos cada valor e lle asignamos a cada clave o seu valor
#con diccionario.get(clave) pra cada iteracción.
for clave in diccionario.keys():
    print("As claves son :"+str(clave)+"E o valor "+ diccionario.get(clave))

elementos = diccionario.items()
#Asignamoslle a elementos todos os items do diccionario para posteriormente recorrelos con duas variables,clave e valor
#e a cada iteraccion printamos cada variable
for clave,valor in elementos:
    print("O valor da clave e "+str(clave)+" e o seu valor "+valor)
#Borramos un elemento pola clave,a través de diccionario.pop
#posteriormente faise un print para comprobar que borrou ese elemento
diccionario.pop(6122)
print(diccionario.items())

"""LISTAS"""
cadea1 ='Exemplo de cadea'
cadea2="Exemplo con doble \n comilla"

print(cadea2.split(" ")) #Separador dunha cadea
print(cadea2.count("co"))#Contador
print(cadea2.find("co",9))#Atopar algo nesa cadea
print(cadea2.partition("\n"))#particiona el print
print(cadea2.replace("\n","&"))#Reemplaza o primeiro parámetro co segundo que poñamos
print(cadea2.join(("*","&","7")))

lista =[22,4.07,"Esto e unha lista",[2,3,4]]

print(lista[2][0:9:2])
print(lista[3])

lista[1] =467.000
print(lista)
lista.append("Uñltimo elemento")
print(lista)

print(lista.count("Idem"))
lista.extend((2,3,4,2,3,2,3,3))#Añade novos parámetros a lista
lista.insert(5,"Esto e unha inserción")#Inserta na posición dada(primeiro parámetro) o que poñamos no segundo parámetro
lista.pop(6)#Elimina o elemento da lista da posición dada por parámetro
lista.remove(467)#Elimina o elemento da lista que teña o valor dado por parámetro
print(lista)
print(lista.count(3))#Conta o número de veces que aparece na lista o parámetro
print(lista.index(2))#Dinos a posición na que se atopa o parámetro
lista.reverse()
print(lista)

lista3 =[2,5,4,9,8,2]
lista3.sort(reverse=True)
print(lista3)
