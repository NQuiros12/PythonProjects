#Metodo encriptado CESAR.
import string
#Cargamos el mensaje.
#fcenGuys = ["Sole","Fi","Joaco","AgusA","AgusB","Vicky","Juli"]
mensaje = """hola como estas zorro, que tal todo hoy."""
mensaje = mensaje.lower()
#Lo metemos dentro de una lista
mensaje = list(mensaje)
#Creamos una lista para el mensaje encriptado
mensajeEncriptado = mensaje
#lista de letras en ascii pero sin ñ
abc = list(string.ascii_lowercase)
abc = abc + ["a","b","c"]
#Creamos la funcion que encripta el mensaje, letra por letra.
def MetodoCesar(letra):
    if(letra == " "):
        return "-"
    elif(letra == "."):
        return "."
    elif(letra == ","):
        return ","
    else:
        return abc[abc.index(letra)+3]
#Creamos un loop que corra por dentro de todas las letras del sistema.
for i in range(len(mensaje)):
    mensajeEncriptado[i] = MetodoCesar(mensaje[i])

print("El mensaje encriptado es")
for numero in mensajeEncriptado:
    print(numero,end = " ")
print("\n" )
