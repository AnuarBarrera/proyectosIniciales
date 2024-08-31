let tipoDeEjercicio = ["pierna","pecho","espalda"];

function llamarEjercicio(tipoDeEjercicio,duracion = 0){
  for(i = 1; i <= duracion; i++){
    document.write(tipoDeEjercicio)
    }
}


llamarEjercicio("pecho",duracion = 8)