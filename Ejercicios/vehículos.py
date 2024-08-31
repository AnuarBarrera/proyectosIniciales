class vehiculo():
  
  def __init__(self,vel,cap,pers):
    self.velocidadMaxima = vel
    self.capacidadPasajeros = cap
    self.nombreConductor = pers
  
  def acelerar(self):
    print("acelere... run, run")
  
  def frenar(self):
    print("frene")
    
  def SubirPasajero(self):
    print("subi a un pasajero")
    
class terrestre(vehiculo):
  
  def __init__(self,vel,cap,pers,mat):
    super().__init__(vel,cap,pers)
    self.matricula = mat

class tren(terrestre,vehiculo):
  
  def __init__(self,vel,cap,pers,mat,vag,ori,dest):
    
    super().__init__(vel,cap,pers,mat)
    self.vagones = vag
    self.origen = ori
    self.destino = dest
    
  def DefinirRuta(self):
    ruta = input('¿a donde vamos?:')
    print(ruta)
    
Salida1 = tren(120,1200,"Juan Hernandez", "ABC123",10,"ciudad de mexico","veracruz")

print(Salida1.destino)
Salida1.acelerar()
Salida1.frenar()
Salida1.SubirPasajero()
Salida1.DefinirRuta()