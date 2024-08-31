const perimeCuadrado = (side) => side * 4;
const AreaCuadrado = (side) => side * side;
const periTriangulo = (side1,side2,side3) => side1 + side2 + side3;
const AreaTriangulo = (base,altura) => (base * altura) / 2
const diametro = (side) => 2 * side;
const perimetroCirculo = (side) => ((2 * 3.14) * side);
const areaCirculo = (side) => (3.14 * (side * side));

function calcularPerimetro(){
  let inputSide = document.getElementById('input-side')
 let value = parseFloat(inputSide.value);
 const resultado = `El perimetro del cuadrado es: ${perimeCuadrado(value)} cm`;
 document.getElementById("respuesta").innerText = resultado;
  
}
function calcularArea(){
  let inputSide = document.getElementById('input-side');
 let value = parseFloat(inputSide.value)
 const resultado = `El área del cuadrado es: ${AreaCuadrado(value)} cm`;
 document.getElementById("respuesta").innerText = resultado;
  
}

function calcularPerimetroTriangulo(){
  let inputSide1 = document.getElementById('side1');
 let value1 = parseFloat(inputSide1.value);
  let inputSide2 = document.getElementById('side2');
 let value2 = parseFloat(inputSide2.value);
  let inputSide3 = document.getElementById('side3');
 let value3 = parseFloat(inputSide3.value);
 const resultado = `El perimetro del triangulo es: ${periTriangulo(value1,value2,value3)} cm`;
 document.getElementById("respuesta").innerText = resultado;
  
}

function calcularAreaTriangulo(){
  let inputBase = document.getElementById("base");
  let valueBase = parseFloat(inputBase.value);
  let inputAltura = document.getElementById("side-altura");
  let valueAltura =parseFloat(inputAltura.value);
 const resultado = ` El area del triangulo es ${AreaTriangulo(valueBase,valueAltura)} cm`;
 document.getElementById("respuesta").innerText = resultado;

}

function diametroCirculo(){
  let inputRadio = document.getElementById("radio");
  let radioValue = parseFloat(inputRadio.value);
  const resultado = `el diametro del circulo es ${diametro(radioValue)} cm`
  document.getElementById("respuesta").innerText = resultado;
}
function AreaCirculo(){
  let inputRadio = document.getElementById("radio");
  let radioValue = parseFloat(inputRadio.value);
  const resultado = `el área del circulo es ${areaCirculo(radioValue)} cm`
  document.getElementById("respuesta").innerText = resultado;
}
function PerimetroCirculo(){
  let inputRadio = document.getElementById("radio");
  let radioValue = parseFloat(inputRadio.value);
  const resultado = `el perimetro del circulo es ${perimetroCirculo(radioValue)} cm`
  document.getElementById("respuesta").innerText = resultado;
}
