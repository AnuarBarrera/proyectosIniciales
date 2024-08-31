const vehiculo{
  constructor (Velocidad_Maxima,Capacidad_Pasajeros,Nombre_Conductor
    ){
      this.Velocidad_Maxima = Velocidad_Maxima;
      this.Capacidad_Pasajeros = Capacidad_Pasajeros;
      this.Nombre_Conductor = Nombre_Conductor;
   }
   
   acelerar(){
     console.log("Acelere... run,run")
   }
   frenar(){
     console.log("frene")
   }
   Subir_Pasajero(){
     console.log("Subi un pasajero")
   }
 }
 
 const terrestre{
   constructor(Matricula){
   this.Matricula = Matricula;
   }
 }
 
 
 Object.assing(vehiculo,terrestre);
 
 const Salida1 = new terrestre(120,1000,"Jose Hernandez","ABC123");
 
 console.log(Salida1.Matricula)
 Salida1.acelerar()
 Salida1.frenar()
 Salida1.Subir_Pasajero()
