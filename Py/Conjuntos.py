#La funcion para crear un conjunto se llama Set() y los argumentos van entre comillas simples '    '
Conjunto = set('846')

#Tambien puede ser definido usando llaves "{ }" y separando por comas 
conjunto1 = {8, 4, 6}

#Operacion de interseccion con operador & 
conjunto_2 = set('785')
Conjunto & conjunto_2 
#Otro ejemplo
Conjunto.interseccion(conjunto_2)

#Si creamos un conjunto con valores repetidos estos seran eliminados automaticamente
duplicados = {2, 3, 6, 7, 6, 8, 2, 1}
duplicados 

#Cadenas de texto 
cadena = "Esto es una cadena de texto"

cad_multiple = ''' Esta es una cadena
de texto que
contiene mas de 
3 cadenas de texto en
una misma variable '''
