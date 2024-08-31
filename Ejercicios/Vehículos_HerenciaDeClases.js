class vehiculo{
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
 
 class terrestre extends vehiculo{
   constructor(Velocidad_Maxima,Capacidad_Pasajeros,Nombre_Conductor,Matricula){
   super(Velocidad_Maxima,Capacidad_Pasajeros,Nombre_Conductor)
   this.Matricula = Matricula;
   }
 }
 
 class tren extends terrestre{
   constructor(Velocidad_Maxima,Capacidad_Pasajeros,Nombre_Conductor,Matricula,vagones,origen,destino){
   super(Velocidad_Maxima,Capacidad_Pasajeros,Nombre_Conductor,Matricula)
   this.vagones = vagones;
   this.origen = origen;
   this.destino = destino;
   }
   definir_ruta(){
   let ruta = prompt("¿a donde vamos?: ")
   console.log(ruta)
   }
 }
 const Salida1 = new tren (120,1000,"Jose Hernandez","ABC123",10,"CDMX","veracruz");
 
 console.log(Salida1.origen)
 Salida1.acelerar()
 Salida1.definir_ruta()
