def convertir(unidadOrigen, valor, unidadDestino):
    if unidadOrigen == "cm":
        if unidadDestino == "in":
            conversion = valor / 2.54
            print("Los " + str(valor) + unidadOrigen + " son: " + str(conversion) + unidadDestino)
    elif unidadOrigen == "m":
        if unidadDestino == "yds":
            conversion = valor * 1.094
            print("Los " + str(valor) + unidadOrigen + " son: " + str(conversion) + unidadDestino)
    elif unidadOrigen == "km":
        if unidadDestino == "mi":
            conversion = valor * 0.621
            print("Los " + str(valor) + unidadOrigen + " son: " + str(conversion) + unidadDestino)
    else:
        print("No se puede realizar la conversión")

# Llamada a la función con los argumentos adecuados
convertir(unidadOrigen, Valor, UnidadDestino)