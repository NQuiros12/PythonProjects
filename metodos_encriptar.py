import string
def metodo_cesar(letra:str)->str:
    """Encripta una letra a partir del metodo cesar"""
    dic_esp = list(string.ascii_lowercase)
    dic_esp.insert(14,"ñ")
    dic_esp = dic_esp + ["a","b","c"]
    if(letra == " " or letra == "\n"):
        return "-"
    elif(letra == "."):
        return "."
    elif(letra == ","):
        return ","
    else:
        return dic_esp[dic_esp.index(letra)+3]
def metodo_cesar_pal(palabra:str)->str:
    """Encripta una palabra a partir del metodo cesar"""
    #Creamos una lista con todas las letras del diccionario diccionario
    dic_esp = list(string.ascii_lowercase)
    dic_esp.insert(14,"ñ")
    dic_esp = dic_esp + ["a","b","c"]
    #Lista con las letras encriptadas listas para encriptar.
    palabra_encri = []
    #Separamos la palabra en letras
    for letra in palabra:
        if(letra == " " or letra == "\n"):
            palabra_encri.append("-")
        elif(letra == "."):
            palabra_encri.append(".")
        elif(letra == ","):
            palabra_encri.append(",")
        else:
            palabra_encri.append(dic_esp[dic_esp.index(letra)+3])
    #Devolvemos la lista unida por un join
    return "".join(palabra_encri)
def desencriptar_cesar_pal(palabra:str)->str:
    """Encripta una palabra a partir del metodo cesar"""
    #Creamos una lista con todas las letras del diccionario diccionario
    dic_esp = list(string.ascii_lowercase)
    dic_esp.insert(14,"ñ")
    dic_esp = dic_esp + ["a","b","c"]
    print(dic_esp.index('b')-3)
    #Lista con las letras encriptadas listas para encriptar.
    palabra_encri = []
    #Separamos la palabra en letras
    for letra in palabra:
        if(letra == " " or letra == "\n"):
            palabra_encri.append("-")
        elif(letra == "."):
            palabra_encri.append(".")
        elif(letra == ","):
            palabra_encri.append(",")
        else:
            #La tecnica de usar el index genera un bug
            print(dic_esp[dic_esp.index(letra)-3],letra)
            palabra_encri.append(dic_esp[dic_esp.index(letra)-3])
    #Devolvemos la lista unida por un join
    return "".join(palabra_encri)
print(desencriptar_cesar_pal("krb"))