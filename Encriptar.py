import string
#Read the message from a txt.
def read_text(filename:str) -> list:
  with open(filename) as f:
    lines = f.readlines()
    #Split the list into words
    lines = [m.split() for m in lines]
    #Flatten the list into just one list of words
    lines = [item for sublist in lines for item in sublist]
    return lines
mensaje = read_text("mensaje.txt")
#lista de letras ahora con ñ
#mensaje = mensaje.split(" ").lower().strip("\n")
print(f"El mensaje es {mensaje}")
#Creamos la funcion que encripta el mensaje, letra por letra.

import metodos_encriptar as mte
mensaje_c = [mte.metodo_cesar_pal(palabra) for palabra in mensaje]
print(" ".join(mensaje_c))
mensaje_d =[mte.desencriptar_cesar_pal(palabra) for palabra in mensaje_c]
print(f"Ahora descrifrado:{mensaje_d}")
#Creamos un loop que corra por dentro de todas las letras del sistema.
# for i in range(len(mensaje)):
#     mensajeEncriptado[i] = MetodoCesar(mensaje[i])
# #Vamos a darle dos pistas a los muchachxs
# print("Pista 1:\n","k == ",MetodoCesar("k"))
# print("Pista 2:\n","w == ",MetodoCesar("w"))
# print("El mensaje encriptado es")
# for numero in mensajeEncriptado:
#     print(numero,end = " ")
# print("\n" )
