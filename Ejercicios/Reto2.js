let consumo, valorImpuesto,montoDescuento,importePago;

consumo = parseFloat(prompt('Ingrese su comsumo: '))

if(consumo<200){
  if(consumo>100){
    montoDescuento = consumo * 0.20
    valorImpuesto = consumo * 0.19
    importePago = consumo - montoDescuento
    importePago = importePago + valorImpuesto
    console.log(`el pago que debe realizar es ${importePago}, al cual se le aplico un descuento del ${montoDescuento} con un impuesto del ${valorImpuesto}`)
  }else{
    montoDescuento = consumo * 0.10
    valorImpuesto = consumo * 0.19
    importePago = consumo - montoDescuento
    importePago = importePago + valorImpuesto
    console.log(`el pago que debe realizar es ${importePago}, al cual se le aplico un descuento del ${montoDescuento} con un impuesto del ${valorImpuesto}`)}
}else{
  montoDescuento = consumo * 0.30
  valorImpuesto = consumo * 0.19
  importePago = consumo - montoDescuento
  importePago = importePago + valorImpuesto
  console.log(`el pago que debe realizar es ${importePago}, al cual se le aplico un descuento del ${montoDescuento} con un impuesto del ${valorImpuesto}`)
}