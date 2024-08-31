let texto = prompt('Ingrese la palabra o frase: ')

function esPalindromo(texto){
  let textoEnMinusculas = texto.toLowerCase()
  let textoJunto = textoEnMinusculas.split('')
  let textoReves = textoJunto.reverse()

  if (textoReves === textoJunto){
    console.log(`${texto} es palindromo`)
  }else{
    console.log(`${texto} no es palindromo`)
  }
}

esPalindromo(texto)