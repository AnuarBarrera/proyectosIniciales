let vv, igv,pv;

vv = prompt('Ingrese el valor: ')
vv = parseFloat(vv)
igv = vv * 0.19
pv = vv + igv

document.write('el igv es: '+ igv +'<br/>')
document.write('El precio de venta es: '+ pv)
