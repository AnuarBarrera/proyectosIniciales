Mensaje1 = "Este es un convertidor de unidades \npodras convertir algunas unidades\ndel sistema métrico al sistema anglosajón"
mensaje2 = "Cada unidad tiene una abreviatura"
mensaje3 = "Las unidades que puedes convertir\n son las siguientes: \n centimetros, metros y kilometros \na pulgadas, yardas y millas"
mensaje4 = "las abreviaturas usadas seran: \n cm,m,km,in,yds y mi"
input(Mensaje1 + "\n" + mensaje2 + "\n"
          + mensaje3 + "\n" + mensaje4)

def validar_unidad(unidad):
  unidades_validas = ["cm", "m", "km", "in", "yds", "mi"]
  if unidad not in unidades_validas:
    raise ValueError("Unidad no válida: " + unidad)

valor = input("Ingrese el valor de la unidad a convertir ")

unidadOrigen = validar_unidad(input("Ingresa la abreviatura de la unidad origen "))

unidadDestino = validar_unidad(input("Ingresa la abreviatura de la unidad destino "))

def convertir(unidadDestino, unidadOrigen, valor):
  try:
    if unidadOrigen == "cm":
      if unidadDestino == "in":
        conversion = valor / 2.5
        return conversion
    elif unidadOrigen == "m":
      if unidadDestino == "yds":
        conversion = valor / 1.094
        return conversion
    elif unidadOrigen == "km":
      if unidadDestino == "mi":
        conversion = valor * 0.621
        return conversion
    else:
      raise ValueError("Conversión no disponible")
  except ValueError as error:
    print(error)
    return None

valor_convertido = convertir(unidadDestino, unidadOrigen, valor)

if valor_convertido is not None:
  print("Los " + valor + " " + unidadOrigen + " son: " + str(valor_convertido) + " " + unidadDestino)

print("Los {valor} {unidad_origen} son: {valor_convertido} {unidad_destino}".format(
  valor=valor,
  unidad_origen=unidadOrigen,
  unidad_destino=unidadDestino,
  valor_convertido=conversion
))
