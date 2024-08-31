#object agenda
class Agenda():
  #create
  def createAgenda(self,agenda):
    for i in range(12):
      if mes[i] in {1,3,5,7,8,10,12}:
        agenda[i] = list(range(1,32))
      elif mes[i] == 2:
        agenda[i] = list(range(1,29))
      else:
        agenda[i] = list(range(1,31))
        
    return agenda
    
  #read
  def readAgenda(self,agenda):
    print(agenda)
  
  #upload
  def uploadAgenda(self,agenda):
    #entrada de datos
    data = input("Ingrese fecha y nombre del evento en formato MM-DD NOMBRE EVENTO")
    
    month = int(data[:2])
    day = int(data[4:6])
    message = data[6:]
    
    month = month - 1
    day = day - 1
    #guardamos en la posicion
    agenda[month][day] = message
    print("agenda actualizada")
    print("Elija la opcion 2 para ver la agenda.")
    
    
  #delete
  def deleteAgenda(self,agenda):
    
    delete = int(input("toda la agenda: 1 \nun registro: 0"))
    
    if delete == 0:
      date = input("ingrese la fecha del registro a eliminar en formato MM-DD")
      month = int(date[:2])
      day = int(date[4:6])
      month = month - 1
      day = day - 1
    #guardamos en la posicion
      agenda[month][day] = date[4:6]
      print("agenda actualizada")
      print("Elija la opcion 2 para ver la agenda.")
    else:
      #es una tramposada porque no modifica la lista 
      print("Agenda vacia, deberas crear una agenda default para continuar")
      


mes = list(range(1,13))
agenda = [0 for _ in range(12)]
menu = int(input("Elige la opcion que deseas:\n1.-crear Agenda default\n2.-ver agenda\n3.-ingresar un registro\n4.elimar la agenda o registro\n5.-finalizar el programa"))



while True:
  
  if menu == 1:
    agenda_obj = Agenda()
    newAgend = agenda_obj.createAgenda(agenda.copy())
    print("agenda Creada\n Elija la opcion 2 para ver la agenda.")
    menu = int(input("Elige la opcion que deseas:\n1.-crear Agenda default\n2.-ver agenda\n3.-ingresar un registro\n4.elimar la agenda o registro\n5.-finalizar el programa"))
  if menu == 2:
    agenda_obj.readAgenda(newAgend)
    menu = int(input("Elige la opcion que deseas:\n1.-crear Agenda default\n2.-ver agenda\n3.-ingresar un registro\n4.elimar la agenda o registro\n5.-finalizar el programa"))
  if menu == 3:
    agenda_obj.uploadAgenda(newAgend)
    menu = int(input("Elige la opcion que deseas:\n1.-crear Agenda default\n2.-ver agenda\n3.-ingresar un registro\n4.elimar la agenda o registro\n5.-finalizar el programa"))
  if menu == 4:
    agenda_obj.deleteAgenda(newAgend)
    menu = int(input("Elige la opcion que deseas:\n1.-crear Agenda default\n2.-ver agenda\n3.-ingresar un registro\n4.elimar la agenda o registro\n5.-finalizar el programa"))
  if menu == 5:
    print("programa concluido")
    break
  