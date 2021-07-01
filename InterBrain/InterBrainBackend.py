import pandas as pd
from tkinter import *
from tkinter import ttk
with open("/home/user/Desktop/reservas.csv") as file:
    reader = pd.read_csv(file)

columns_tokeep = ["nombre","horarios"]
df= reader[columns_tokeep]
df= df.dropna()
reservas = dict(zip(df.nombre,df.horarios))
lista_de_horarios= list(reader["horario"])
def comboclick_sala(*args):
    global sala_deseada
    sala_deseada = boxCombo_Sala.get() 
    if sala_deseada == "Sala 1":
        file_dir = ("/home/user/Desktop/sala1.csv")
    elif sala_deseada == "Sala 2":
        file_dir = ("/home/user/Desktop/sala2.csv")
    else:
        file_dir = ("/home/user/Desktop/sala3.csv")
        

        
clicked1= StringVar()
clicked1.set("sala1")

boxCombo_Sala= ttk.Combobox(ventana, value=["Sala 1","Sala 2","Sala 3"])
boxCombo_Sala.current(0)
boxCombo_Sala.bind("<<ComboboxSelected>>",comboclick_sala)
boxCombo_Sala.grid(row=0,column=0)
#reservas= {"Howard Lovecraft":"22:00",
    #"Pablo Quirós":"18:00",
    #"Julieta Trape":"19:00"}
#lista_de_horarios = list(range(11,22,1))
def reserva(reservas,lista_de_horarios):
    decision = input("Reserva o chequeo: ")
    decision = decision.lower()
    if decision == "reserva":
        nombreCliente = input("Nombre del cliente")
        horario_deseado= input("Horario para la reserva")
  
        for key,value in reservas.items():
            if horario_deseado == value:
                print("Ese horario ya esta reservado, disculpe. Reingrese el horario")
                break
            else:
                print("Horario reservado de manera satisfactoria")
                dic1={nombreCliente:horario_deseado,}
            #print(dic1)
                reservas.update(dic1)
                break
    if decision == "chequeo":
        nombreCliente = input("Nombre")
        for key,value in reservas.items():
            if nombreCliente == key:
                print("La reserva a nombre de",nombreCliente,"es para las",value)
                break
            else:
                continue
        else:
            print("No se encuentra el nombre.")
sala1 = reserva(reservas,lista_de_horarios)

   
      