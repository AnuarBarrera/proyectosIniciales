let valor = 29;

function validaPerfectos(valor){
  
  if(valor > 1){
    let sumaDeValor = 0;
    for(let i = 1; i <= valor / 2; i++){
      if(valor % i == 0){
        sumaDeValor += i;
      }
    }
    
    if(sumaDeValor == valor){
    console.log('felicidades',valor,'es perfecto')
    }else{
    console.log(valor,'no es perfecto')
    }
    
  }else{
    console.log("Ingrese un número valido, mayor a 1")
  }
}

validaPerfectos(valor)