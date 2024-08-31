Mensaje1 = "Este es un convertidor de unidades \npodras convertir algunas unidades\ndel sistema métrico al sistema anglosajón"
mensaje2 = "Cada unidad tiene una abreviatura"
mensaje3 = "Las unidades que puedes convertir\n son las siguientes: \n centimetros, metros y kilometros \na pulgadas, yardas y millas"
mensaje4 = "las abreviaturas usadas seran: \n cm,m,km,in,yds y mi"
input(Mensaje1 + "\n" + mensaje2 + "\n"
    + mensaje3 + "\n" + mensaje4)
unidadOrigen = input("Ingresa la abreviatura de la unidad origen ")
Valor = input("ingresa el valor a convertir ")
UnidadDestino = input("Ingresa la abreviatura de la unidad destino ")

def covertir(unidadDestino,unidadOrigen,valor):
  if unidadOrigen == "cm":
    if unidadDestino == "in":
      conversion = valor / 2.5
      print("los" + valor + unidadDestino + "son: " + conversion + unidadDestino)
#  elif unidadOrigen == "m":
#     if unidadDestino == "yds":
#        conversion = valor / 1.094
#        print("los" + valor + unidadDestino + "son: " + conversion + unidadDestino)
#  else:
#      conversion = valor * 0.621
#      print("los" + valor + unidadDestino + "son: " + conversion + unidadDestino)
  
  
convertir(unidadOrigen,UnidadDestino,Valor)