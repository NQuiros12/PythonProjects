#Metodo encriptado cesar.
import string
#Cargamos el mensaje.
#fcenGuys = ["Sole","Fi","Joaco","AgusA","AgusB","Vicky","Juli"]
mensaje = """Les queria agradecer por este gran año juntos, por bancarme siempre en todas mis ideas. 
Por darme animos para cada uno de mis proyectos. Gracias por dejarme ser quien soy sin juzgarme nunca. Los amo"""
mensaje = mensaje.lower()
#Lo metemos dentro de una lista
mensaje = list(mensaje)
#Creamos una lista para el mensaje encriptado
mensajeEncriptado = mensaje
#lista de letras en ascii pero sin ñ
abc = list(string.ascii_lowercase)
#Creamos la funcion que encripta el mensaje, letra por letra.
def VocaloConsonante(letra):
    if(letra =="a" or
        letra == "e" or letra == "i" or
         letra == "o" or letra == "u"):
         return abc.index(letra)
    elif(letra == "ñ"):
        return "ñ"
    elif(letra == " "):
        return " "
    elif (letra == "."):
        return "."
    elif(letra == ","):
        return ","
    elif(letra == "\n"):
        return "\n"
    else:
        return abc.index(letra)-1
#Creamos un loop que corra por dentro de todas las letras del sistema.
for i in range(len(mensaje)):
    mensajeEncriptado[i] = VocaloConsonante(mensaje[i])

print("El mensaje encriptado es")
for numero in mensajeEncriptado:
    print(numero,end = "/")
print("\n")
