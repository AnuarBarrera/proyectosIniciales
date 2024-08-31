let producto = parseFloat(prompt("ingrese precio:"));
const impuesto = 0.07;
producto = producto += producto * impuesto
producto *= 0.85
console.log(producto)