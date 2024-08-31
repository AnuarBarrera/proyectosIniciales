from Operaciones import convertir

Mensaje1 = "Este es un convertidor de unidades \npodras convertir algunas unidades\ndel sistema métrico al sistema anglosajón"
mensaje2 = "Cada unidad tiene una abreviatura"
mensaje3 = "Las unidades que puedes convertir\n son las siguientes: \n centimetros, metros y kilometros \na pulgadas, yardas y millas"
mensaje4 = "las abreviaturas usadas seran: \n cm,m,km,in,yds y mi"
input(Mensaje1 + "\n" + mensaje2 + "\n"
    + mensaje3 + "\n" + mensaje4)
unidadOrigen = input("Ingresa la abreviatura de la unidad origen ")
Valor = input("ingresa el valor a convertir ")
UnidadDestino = input("Ingresa la abreviatura de la unidad destino ")

convertir(unidadOrigen,UnidadDestino,Valor)
