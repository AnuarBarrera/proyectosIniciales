#readmy CalculadoraDeNutricion is un algoritm what calculate the content protein, sugar and fats have the product.

#SE DEBE CORREGIR LA HERENCIA ENTRE LAS 2 CLASES

class CalculadoraDeNutricion():
  def __init__(self):
    #Entrance Information
    def inputInformation(self):
      return input("you write the count from grams the sample, portion, sugar, protein and fats in that order and separated with comma (ejem: 100,150,80, etc")
   
  #DataBase
  def ChargeDataBase(self,variables,DictionaryVariables):
    return dict(zip(DictionaryVariables.keys(),variables))
    
  #Calculations
  def calculate(self):
    pass
    
  #Exit Information
  def showResult(self):
    pass

#Class mmMenu show message the user

class Menu(CalculadoraDeNutricion):
  def __init__(self):
    super().__init__()
  
  def messageWelcome(self):
    print ("Welcome to Calculadora De Nutricion\nI will help to calculate the content\nwhit Proteins, Sugar and fat from any product\nYou get into some data\nfor know the nutrimental value from the product")
    


start = Menu()
start.messageWelcome()
variables = start.inputInformation()
DictionaryVariables = {"sample: ","portion: ","sugar: ","protein: ","sugar: "}
data = star.ChargeDataBase(variables,DictionaryVariables)


    

    
    
