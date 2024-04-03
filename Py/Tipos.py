'''Referencias en strings (PENDIENTE POR AGREGAR MAS TEXTO)'''
#Para declarar un string tipo byte, basta con anteponer la leta b antes de las comillas 
cad = b"Cadena de texto tipo byte"
type(cad)

#El siguiente ejemplo utiliza la codificacion de caracteres 
#latin1 para crear un string de este tipo 
lat = bytearray("España", 'latin1')
print(lat)
bytearray("España", "utf16")

#Aqui veremos como convertir de str a byte y viseversa con las funciones 
# ".encode" para convertir a byte y ".decode" para convertir a str
cadena = "Pasara a byte"
cadena.encode()
print(type, cadena)

cadena2 = b"Pasara a str"
cadena2.decode()

'''Estos solo se encuentran definidos para
cada tipo. Esto significa que decode() no existe para el tipo str y que 
encode() no funciona para el tipo de byte'''
