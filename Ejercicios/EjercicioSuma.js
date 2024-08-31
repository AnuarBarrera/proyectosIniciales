function sumar(...args){
  let suma = 0;
  for (let n of args){
    suma += n;
  }
  return suma
}

x = sumar(1,1,1,1)

console.log(x)