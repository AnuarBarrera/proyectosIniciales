class Products():
  
  def listProductsDefault(self):
    listDefault = {"milk": 5,"eggs":20,"chicken beef": 10,"cow beef":25}
    print("lista creada")
    return listDefault
    
  def newList(self):
    listNew = {}
    element = input("ingrese el producto: ")
    count = int(input("ingrese la cantidad: "))
    
    while element != "":
      listNew.update([(element,count)])
      print("producto agregado")
      element = input("ingrese el producto: ")
      count = int(input("ingrese la cantidad: "))
  
    return listNew
    
  def deleteProduct(self,listNew):
    number = print("indique el producto del cual desea eliminar 1 elemento: ")
    listNew.pop(number)
    print("elemento eliminado")
    return listNew
    
  def viewList(self,List):
    list.values()

print("almacen")

menu = input("ingrese la opcion deseada\n1.Crear lista default\n2.Visualizar lista\n3.Crear Lista\n4.Eliminar elemento\n")

while True:
  
  if menu == 1:
    market = Products()
    newObject = market.listDefault()
    menu = input("ingrese la opcion deseada\n1.Crear lista default\n2.Visualizar lista\n3.Crear Lista\n4.Eliminar elemento: ")
  if menu == 2:
    market.viewList(newObject)
    menu = input("ingrese la opcion deseada\n1.Crear lista default\n2.Visualizar lista\n3.Crear Lista\n4.Eliminar elemento: ")
  if menu == 3:
    newObjet = market.listNew()
    menu = input("ingrese la opcion deseada\n1.Crear lista default\n2.Visualizar lista\n3.Crear Lista\n4.Eliminar elemento: ")
  if menu == 4:
    market.deleteProduct(newObject)
    menu = input("ingrese la opcion deseada\n1.Crear lista default\n2.Visualizar lista\n3.Crear Lista\n4.Eliminar elemento: ")