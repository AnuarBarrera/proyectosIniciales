let Enteros =[1,2,3,4,5,6,7,8,9], pares = [],impares[], contador = 0,multiplicacion = 0, multiplicador = random(1,100)

for enteros(contador){
  multiplicacion = enteros * multiplicador
  multiplicacion % 2 === 0 : pares.pop(multiplicacion) | impares.pop(multiplicacion)
  ++contador
  console.log(`${entero} x ${multiplicador} = ${multiplicacion} pares = ${pares} impares = ${impares}`)
}