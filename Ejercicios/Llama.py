class Products():
    def listProductsDefault(self):
        listDefault = {"milk": 5, "eggs": 20, "chicken beef": 10, "cow beef": 25}
        print("Lista creada")
        return listDefault

    def newList(self):
        listNew = {}
        while True:
            element = input("Ingrese el producto (o presione Enter para salir): ")
            if element == "":
                break
            count = int(input("Ingrese la cantidad: "))
            listNew.update({element: count})
            print("Producto agregado")
        return listNew

    def deleteProduct(self, listNew):
        print("Indique el producto del cual desea eliminar 1 elemento: ")
        for i, product in enumerate(listNew.keys()):
            print(f"{i+1}. {product}")
        number = int(input("Ingrese el número del producto: ")) - 1
        if number < len(listNew):
            del listNew[list(listNew.keys())[number]]
            print("Elemento eliminado")
        else:
            print("Número inválido")
        return listNew

    def viewList(self, List):
        for product, count in List.items():
            print(f"{product}: {count}")
        print("Almacen")

def main():
    market = Products()
    while True:
        print("\nIngrese la opción deseada:")
        print("1. Crear lista default")
        print("2. Visualizar lista")
        print("3. Crear Lista")
        print("4. Eliminar elemento")
        print("5. Salir")
        option = input("Opción: ")
        if option == "1":
            newObject = market.listProductsDefault()
        elif option == "2":
            market.viewList(newObject)
        elif option == "3":
            newObject = market.newList()
        elif option == "4":
            newObject = market.deleteProduct(newObject)
        elif option == "5":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
