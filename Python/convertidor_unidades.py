print("Hola. Este es un convertidor de unidades. Ingresa el valor y las unidades de medida y yo te ayudare a convertirlo")
print(
    "Las unidades que puedo convertir estan clasificadas por magnitudes: Longitud, Área, Fuerza, Energia, Tiempo, Volumen, Potencia, Presión, Masa, Velocidad y Densidad")

vConvertir = input("Ingresa el valor a convertir: ")

print("Ingresa la magnitud para indicarte las unidades que puedes convertir.")

magnitud = input("Ingresa la magnitud: ")

longitud = "Milimetro (ml), Centimetro(cm), Metro(m), Kilometro(km), Pulgada(pl), Pie(p), Milla(ma)"
tiempo = "Segundos(s), Minutos(m), Horas(h), Dias(d), Meses(ms), Años(a)"
masa = "Miligramos(mg), Gramos(g), Kilogramos(kg), Toneladas(t), Onza(oz), Libras(lb)"
area = "Centimetros Cuadrados(cm2), Metros Cuadrados(m2), Hectaria(h), Pulgada Cuadrada(p2), Pie Cuadrado(pie2), Milla Cuadrada (ma2)"
volumen = "Centimetro Cubico(cm3), Metro Cubico(m3), Litro(l), Pulgada Cubica(p3), Pie Cubico(pie3)"
velocidad = "Metro por Segundo(m/s), Kilometro por Hora(k/h), Pie por Segundo(pie/s), Milla por Hora(m/h)"
fuerza = "Newton(nw), Libra(lb)"
potencia = "Vatio(v), Caloria por Segundo(c/s), Caballo de Vapor(cv), Pie-Libra por Segundo(pie/lb)"
densidad = "Gramo por Metro Cubico(g/m3), Kilogramo por Metro Cubico(k/m3), Libra por Metro Cubico(lb/m3)"
energia = "Juls(j), Caloria(c), KiloVatio Hora(kv/h)"
presion = "Pascal(p), Atmosfera(atms), Milimetro de Mecurio(ml/mg)"


def validar_mag(magnitud):
    if magnitud == "longitud":
        print(longitud)
    if magnitud == "tiempo":
        print(tiempo)
    if magnitud == "masa":
        print(masa)
    if magnitud == "area":
        print(area)
    if magnitud == "volumen":
        print(volumen)
    if magnitud == "velocidad":
        print(velocidad)
    if magnitud == "fuerza":
        print(fuerza)
    if magnitud == "potencia":
        print(potencia)
    if magnitud == "densidad":
        print(densidad)
    if magnitud == "energia":
        print(energia)
    if magnitud == "presion":
        print(presion)


validar_mag(magnitud)

print("ingresa las letras marcadas entre parentesis para hacer la conversion.")
magnitud1 = input("Magnitud origen: ")
magnitud2 = input("Magnitud destino: ")

def convertir(magnitud,vConvertir, magnitud1, magnitud2):
    resultado = ""
    if magnitud == "longitud" and magnitud1 == "ml" and magnitud2 == "cm":
        resultado = vConvertir * 0.1 
        return resultado
