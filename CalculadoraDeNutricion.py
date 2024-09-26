#readmy CalculadoraDeNutricion is un algoritm what calculate the content protein, sugar and fats have the product.

#Class Usuario show interface the usuario
class Usuario():
  
  def messageWelcome(self):
    print ("Welcome to Calculadora De Nutricion\nI will help to calculate the content\nwhit Proteins, Sugar and fat from any product\nYou get into some data\nfor know the nutrimental value from the product")
  
  #Entrance Information
  def inputInformation(self):
    return input("you write the count from grams the sample, grams wiht product, sugar, protein and fats in that order and separated with comma (ejem: 100,150,80, etc")
    
  #Exit Information
  def showResult(self,resultSugar,resultProtein,resultFat):
    print(f"The count from sugar is {resultSugar:.2f}, from protein {resultProtein:.2f} and fats {resultFat:.2f}")
  
#Class TransformData is one implementation between the entrence information and el process data in CalculadoraDeNutricion
class TransformData():
  
  def transformateList(self,data):
    dataList = [float(x) for x in data.split(",")]
    return dataList
  
  def transform(self,data,number):
    
    value = 0
    
    for i in range(0,5):
      if i == number:
        value = data[i]
        
    return value
    
#class CalculadoraDeNutricion is the backend from application
class CalculadoraDeNutricion():
 
  #Calculations
  def calculate(self,sample,portion,incognit):
    return (portion * incognit) / sample

#Manager execptions

class Execptions():
  
  def wordsNoAcepted(self):
    pass
  
  def valuesMinimus(self):
    pass
  
  def pointForComma(self):
    pass
  
#call the start app
startApp = Usuario()
startApp.messageWelcome()
dataUsurio = startApp.inputInformation()

#call transformate data
transfomData = TransformData()
informationList = transfomData.transformateList(dataUsurio)

#call exeprions

#charge the variables
sample = transfomData.transform(informationList,0)
portion = transfomData.transform(informationList,1)
sugar = transfomData.transform(informationList,2)
protein = transfomData.transform(informationList,3)
fat = transfomData.transform(informationList,4)

#calculus, processing data
result = CalculadoraDeNutricion()
resultSugar = result.calculate(sample,portion,sugar)
resultProtein = result.calculate(sample,portion,protein)
resultFat = result.calculate(sample,portion,fat)

#show results
startApp.showResult(resultSugar,resultProtein,resultFat)
