n = prompt('Ingrese el número: ')

function esPrimo(n) {
  if (n <= 1) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return console.log(`${n} no es primo`);
  }
  return console.log(`${n} es primo`);
}

esPrimo(n);

