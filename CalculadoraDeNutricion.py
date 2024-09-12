#readmy CalculadoraDeNutricion is un algoritm what calculate the content protein, sugar and fats have the product.

class CalculadoraDeNutricion ():
  #variables
  gramsExent = 0.0
  portion = 0.0
  sugar = 0.0
  protein = 0.0
  fats = 0.0
  result = 0.0
  
  #Entrance Information
  def inputInformation(self):
    pass
  #Calculations
  def calculate(self):
    pass
    
  #Exit Information
  def showResult(self):
    pass

#abstraction, User interface is diferent to the process operations

class menu():
  
  def messageWelcome(self):
    print ("Welcome to Calculadora De Nutricion\nI will help to calculate the content\nwhit Proteins, Sugar and fat whit any product\nYou get into some data\nfor know the nutrimental value whit the product")
    
  def showOptions(self):
    pass
    
  def inputOption(self):
    pass

callTheMessageWelcome = menu()
callTheMessageWelcome.messageWelcome()
    

    
    
