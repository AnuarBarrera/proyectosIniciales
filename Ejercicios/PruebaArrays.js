//entrada

const decimales = [1.78, 2.9748, 3.654, 1.3726, 4.22827];

//operaciones

let NumeroDePosiciones = decimales.length;
let valorMinimo = Math.min(...decimales);
let valorMaximo = Math.max(...decimales);

function promedio(numeros) {
  
  let valor = 0;
  
  for (let i = 0; i < NumeroDePosiciones; i++) {
    
    valor += numeros[i];
    
  }
  const promedio = valor / NumeroDePosiciones;
  return promedio
}

let prom = promedio(decimales)

console.log(`${valorMaximo} es el numero mas grande del array, ${valorMinimo} es el valor mas pequeño del array y ${prom} es el promedio`)