#readmy CalculadoraDeNutricion is un algoritm what calculate the content protein, sugar and fats have the product.

#Class Usuario show interface the usuario
class Usuario():
  
  def messageWelcome(self):
    print ("Welcome to Calculadora De Nutricion\nI will help to calculate the content\nwhit Proteins, Sugar and fat from any product\nYou get into some data\nfor know the nutrimental value from the product")
  
  #Entrance Information
  def inputInformation(self):
    return input("you write the count from grams the sample, portion, sugar, protein and fats in that order and separated with comma (ejem: 100,150,80, etc")
    
  #Exit Information
  def showResult(self):
    pass
  
#Class TransformData is one implementation between the entrence information and el process data in CalculadoraDeNutricion
class TransformData():
  
  def transformateList(self,data):
    dataList = [int(x) for x in data.split(",")]
    return dataList
  
  def transform(self,data,number):
    
    value = 0
    
    for i in range(0,4):
      if i == number:
        value = data[i]
        
    return value
    
#class CalculadoraDeNutricion is the backend from application
class CalculadoraDeNutricion():
  def __init__(self,sample,portion,incognit):
    self.sample = sample
    self.portion = portion
    self.incognit = incognit
 
  #Calculations
  def calculate(self,sample,portion,incognit):
    return (portion * incognit) / sample

startApp = Usuario()
startApp.messageWelcome()
dataUsurio = startApp.inputInformation()
transfomData = TransformData()
informationList = transfomData.transformateList(dataUsurio)
sample = transfomData.transform(informationList,0)
portion = transfomData.transform(informationList,1)
sugar = transfomData.transform(informationList,2)
protein = transfomData.transform(informationList,3)
fat = transfomData.transform(informationList,4)

