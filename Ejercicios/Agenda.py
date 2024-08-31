#matriz
agenda = [[[[0 for _ in range(24)] for _ in range(31)] for _ in range(12)] for _ in range(5)]
#funcion
def programing():
  #entrada de datos
  data = input("Ingrese fecha, hora y nombre del evento en formato AAAA-MM-DD HH:MM NOMBRE EVENTO")

  anios = [2024,2025,2026,2027,2028]
  
  year = int(data[0:4])
  month = int(data[6:7])
  day = int(data[9:10])
  hour = int(data[11:12])
  message = data[17:]
  #iteramos para obtener el indice
  for i in range(4):
    if anios[i] == year:
      year = i
  
  month = month - 1
  day = day - 1
  hour = hour
  #guardamos en la posicion
  agenda[year][month][day][hour] = message
#llamda a funcion  
programing()

print(agenda)


          