import random
def comparaLista(lista,k):

    iguais = []
    maiores = []
    menores = []

    for elemento in lista:
     if elemento==k:
         iguais.append(elemento)
     elif elemento>k:
         maiores.append(elemento)
     else:
         menores.append(elemento)


    return maiores,iguais,menores

listaExemplo = [1,2,3,4,5,6,7,7,7,8,9,10]


l1,l2,l3 = comparaLista(listaExemplo,7)

print(l1)
print(l2)
print(l3)


#exercicio 14

def contaPalabras(cadea):
    palabras = cadea.split()
    diccionario = dict()
    for palabra in palabras:
        if not palabra in diccionario:
            repeticions=0
            for elemento in palabras:
                if elemento == palabra:
                    repeticions = repeticions+1
            diccionario[palabra] = repeticions

    return diccionario


def contaPalabras2(cadea):
    palabras = cadea.split()
    diccionario = dict()
    for palabra in palabras:
        if palabra in diccionario:
           diccionario[palabra]= diccionario[palabra]+1
        else:
         diccionario[palabra] = 1

    return diccionario


print (contaPalabras("Hola que tal amigos,que imos facer hoxe?"))
print(contaPalabras2("Hola que tal amigos,que imos facer hoxe?"))




#15
def tiradasDados(veces):
    tiradas = list()
    for tirada in range(veces+1):
     tirada1 = random.randrange(1,6)
     tirada2 = random.randrange(1,6)
     tiradas.append((tirada1,tirada2))
    return tiradas

def contaValorTiradas(tiradasDados):
    cuentaTiradas = dict()
    for tirada in tiradasDados:
        valor = tirada[0]+tirada[1]
        if valor in cuentaTiradas:
          cuentaTiradas[valor] = cuentaTiradas[valor]+1
        else:
            cuentaTiradas[valor]=1

    return cuentaTiradas



print(contaValorTiradas(tiradasDados(5)))
