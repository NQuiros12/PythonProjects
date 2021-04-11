import pandas as pd
from tkinter import *
from tkinter import ttk
with open("/home/user/Desktop/reservas.csv") as file:
    reader = pd.read_csv(file)

columns_tokeep = ["nombre","horario"]
df= reader[columns_tokeep]
df= df.dropna()
reservas = dict(zip(df.nombre,df.horario))
horarios=list(reader["horarios"]) #
#["11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00"]
#Frontend
#Creamos la ventana

ventana = Tk()
ventana.geometry("780x200")
ventana.configure(bg="beige")
ventana.title("Reservar turnos")
ttk.Button(ventana, text='Salir', command=ventana.destroy).grid(row=4,column=4)

#Nombre Cliente
caja_texto= Entry(ventana)
caja_texto.grid(row=0,column=0)
def CajaNombreCliente():
    global nombreCliente
    nombreCliente = caja_texto.get()
    return nombreCliente
    #print(nombreCliente)
boton1 = Button(ventana,text="Insertar Nombre",padx=4,pady=5,command=CajaNombreCliente)
boton1.grid(row=0,column=1)
#Sala
def comboclick_sala(*args):
    global sala_deseada
    sala_deseada = boxCombo_Sala.get()
    global file_dir
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
boxCombo_Sala.grid(row=1,column=2)
#Horarios

def comboclick(*args):
    for key in reservas:
        global horario_deseado
        
        horario_deseado = boxCombo.get()
        
        if horario_deseado not in reservas.values():
            #print(horario_deseado)
            Label(ventana,text="Horario reservado con normalidad").grid(row=2,column=3)
            dic1={nombreCliente:horario_deseado,}
            reservas.update(dic1)
            df_reservas = pd.DataFrame(reservas.items(),columns=columns_tokeep)
            df_reservas.to_csv(file_dir)
            break
        else:
            Label(ventana,text="Ese horario ya esta reservado. Intente nuevamente").grid(row=2,column=2)

        
clicked= StringVar()
clicked.set(horarios[0])

boxCombo= ttk.Combobox(ventana, value=horarios)
boxCombo.current(0)
boxCombo.bind("<<ComboboxSelected>>",comboclick)
boxCombo.grid(row=2,column=2)
#Salas

ventana.mainloop()#Corremos la imagen