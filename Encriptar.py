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
#lista de letras ahora con ñ
abc = list(string.ascii_lowercase)
abc.insert(14,"ñ")
abc = abc + ["a","b","c"]
#Creamos la funcion que encripta el mensaje, letra por letra.
def MetodoCesar(letra):
    if(letra == " " or letra == "\n"):
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
#Vamos a darle dos pistas a los muchachxs
print("Pista 1:\n","k == ",MetodoCesar("k"))
print("Pista 2:\n","w == ",MetodoCesar("w"))
print("El mensaje encriptado es")
for numero in mensajeEncriptado:
    print(numero,end = " ")
print("\n" )
