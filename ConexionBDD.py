import sqlite3 as dbapi

print("Versión da api :"+dbapi.apilevel)
"""
threadsafety
0   Threads may not share the module.
1 	Threads may share the module, but not connections.
2 	Threads may share the module and connections.
3 	Threads may share the module, connections and cursors."""
print(dbapi.threadsafety)
"""Paramstyle :
Define """
print(dbapi.paramstyle)
#Creamos objeto para la conexión de bbdd,le pasamos el nombre del archivo siempre terminado por .dat
#try -except el nombre del objeto a atrapar seguido del punto y el tipo de error

try:
  bbdd = dbapi.connect("bbdd.dat")
  print(bbdd)

  cursor = bbdd.cursor()
  print (cursor)
  #Creación de una tabla


  #cursor.execute("""create table usuarios

                    #(dni text,nome text,direccion text)""")

         # Esto es para crear la base de datos con un try catch,en este caso saltará el databaseError dado que a base de datos xa existe e intenta creala
#ao executalo programa.

  cursor.execute("insert into usuarios VALUES ('333333-A','Pepe','García Barbón')")
  cursor.execute("insert into usuarios VALUES ('333333-B','Ana','Rosalía De Castro')")
  bbdd.commit()
  cursor.execute("Select * from usuarios")
  for rexistro in cursor.fetchall():
    print("\nDNI :"+rexistro[0])
    print("Nome"+rexistro[1])
    print("Dirección :"+rexistro[2])
  print(cursor.fetchone())

  cursor.execute("Select * from usuarios")
  for rexistro in cursor.fetchmany():
    print("\nDNI :" + rexistro[0])
    print("Nome" + rexistro[1])
    print("Dirección :" + rexistro[2])


except dbapi.DatabaseError as erroOperacion:
    print("Uups parece que temos un problemiña"+erroOperacion)
except dbapi.outraExcepcion:
    print("Tratamento propio de excepción")


