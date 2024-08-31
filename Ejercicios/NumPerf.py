valor = 6

def ValidarPerfectos(valor):
  if valor > 1:
    for i in valor:
      print('pase por for')
  else:
    print('ingresa un número valido, mayor a 1')
    
ValidarPerfectos(valor)