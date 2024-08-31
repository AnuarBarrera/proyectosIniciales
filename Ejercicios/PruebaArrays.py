#entrada

decimales = [1.78,2.9748,3.654,1.3726,4.22827]

#operaciones

NumeroDePosiciones = len(decimales)

valorMinimo = min(decimales)
valorMaximo = max(decimales)

def promedio(decimales):
  valor = 0
  for i in decimales:
    valor += i
    return valor
  
  promedio = valor / NumeroDePosiciones
  return promedio

#salida

promedio = promedio(decimales)
print(f"{valorMinimo} es el valor minimo \n {valorMaximo} es el valor maximo \n {promedio} es el promedio de los numeros")
  
  
