function factorial(n){
  if (n > 1){
    //console.log(n)
    n = n * factorial(n - 1)
    //console.log(n)
  }
    return n
}
 console.log(factorial(7))