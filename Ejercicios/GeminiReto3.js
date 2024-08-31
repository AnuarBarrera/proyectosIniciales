const Enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const pares = [];
const impares = [];
let contador = 0;
let multiplicacion = 0;
const multiplicador = Math.floor(Math.random() * 100) + 1; // Generate random number between 1 and 100 (inclusive)

for (const entero of Enteros) {
  multiplicacion = entero * multiplicador;

  if (multiplicacion % 2 === 0) {
    pares.push(multiplicacion); // Add even number to 'pares' array
  } else {
    impares.push(multiplicacion); // Add odd number to 'impares' array
  }

  contador++;
  console.log(`${entero} x ${multiplicador} = ${multiplicacion} pares = ${pares} impares = ${impares}`);
}
