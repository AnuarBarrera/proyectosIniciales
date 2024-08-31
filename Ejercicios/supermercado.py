class Supermarket():
  
  def payBoxes(self, unit):
    payBoxes = [[] for _ in range(unit)]
    return payBoxes
  
  def index(self,payBoxes,unit):
    for i in range(unit):
      cliente = payBoxes[i][0]
      print(cliente)
        
  def RequestCostumers(self,payBoxes,unit):
    for i in range(unit):
      for j in range(int(len(payBoxes[i]))):
        cliente = payBoxes[i][j]
        print(cliente)
        
  def newCustomer(self,payBoxes):
    box = int(input("indica el numero de la caja a la cual deseas que ingrese el cliente: "))
    box = box - 1
    payBoxes[box].append("cliente")
    print("cliente agreagado")
    
  def customerAttachment(self,payBoxes):
    box = int(input("indica el numero de la caja de la cual deseas sea atendido el cliente: "))
    box = box - 1
    payBoxes[box].pop(0)
    print("cliente atendido")
    

print("bienvendido al Supermercado")
menu = int(input("Elige la opcion que deseas:\n1.-Abrir cajas\n2.-ingresar un cliente\n3.-Atender un cliente\n4.-finalizar el programa"))


while True:
  
  if menu == 1:
    unit = int(input("Indique el numero de cajas: "))
    market = Supermarket()
    newObject = market.payBoxes(unit)
    print("Supermercado abierto\n se crearon ", unit," numero de cajas")
    menu = int(input("Elige la opcion que deseas:\n1.-Abrir cajas\n2.-ingresar un cliente\n3.-Atender un cliente\n4.-finalizar el programa"))
  if menu == 2:
    market.newCustomer(newObject)
    menu = int(input("Elige la opcion que deseas:\n1.-Abrir cajas\n2.-ingresar un cliente\n3.-Atender un cliente\n4.-finalizar el programa"))
  if menu == 3:
    market.customerAttachment(newObject)
    menu = int(input("Elige la opcion que deseas:\n1.-Abrir cajas\n2.-ingresar un cliente\n3.-Atender un cliente\n4.-finalizar el programa"))
  if menu == 4:
    print("programa concluido")
    break
 




