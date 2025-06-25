import tkinter as tk
from tkinter import messagebox

lock = False

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("352x600")
ventana.config(bg="white")
ventana.resizable(False, False)

label_op = tk.Label(ventana, anchor="e", text="", font=("Arial", 20), bg="white", fg="gray")
label_op.pack(fill="x", padx= 15, anchor="e")
label_res = tk.Label(ventana, anchor = "e", text="0", font=("Arial", 65), bg = "white")
label_res.pack(fill="x", padx = 15, pady = 15, anchor="e")

boton0 = tk.Button(ventana, text="0", font=("Arial", 20), width=5, height=2)
boton1 = tk.Button(ventana, text="1", font=("Arial", 20), width=5, height=2)
boton2 = tk.Button(ventana, text="2", font=("Arial", 20), width=5, height=2)
boton3 = tk.Button(ventana, text="3", font=("Arial", 20), width=5, height=2)
boton4 = tk.Button(ventana, text="4", font=("Arial", 20), width=5, height=2)
boton5 = tk.Button(ventana, text="5", font=("Arial", 20), width=5, height=2)
boton6 = tk.Button(ventana, text="6", font=("Arial", 20), width=5, height=2)
boton7 = tk.Button(ventana, text="7", font=("Arial", 20), width=5, height=2)
boton8 = tk.Button(ventana, text="8", font=("Arial", 20), width=5, height=2)
boton9 = tk.Button(ventana, text="9", font=("Arial", 20), width=5, height=2)
boton_punto = tk.Button(ventana, text=".", font=("Arial", 20), width=5, height=2)
boton_signo = tk.Button(ventana, text="+/-", font=("Arial", 20), width=5, height=2)
boton_mas = tk.Button(ventana, text="+", font=("Arial", 20), width=5, height=2)
boton_menos = tk.Button(ventana, text="-", font=("Arial", 20), width=5, height=2)
boton_div = tk.Button(ventana, text="/", font=("Arial", 20), width=5, height=2)
boton_mult = tk.Button(ventana, text="*", font=("Arial", 20), width=5, height=2)
boton_igual = tk.Button(ventana, text="=", font=("Arial", 20), width=5, height=2)
boton_back = tk.Button(ventana, text="<---", font=("Arial", 20), width=5, height=2)
boton_c = tk.Button(ventana, text="C", font=("Arial", 20), width=5, height=2)
boton_ce = tk.Button(ventana, text="CE", font=("Arial", 20), width=5, height=2)

def agregar_texto(boton):
    if(label_res.cget("text") == "0" and boton.cget("text") == "0"):
        return
    elif ((len(label_res.cget("text")) == 1 and label_res.cget("text") == "0")):
        label_res.config(text="")
        nuevo_texto = label_res.cget("text") + boton.cget("text")
        label_res.config(text=nuevo_texto)
        return
    else:
        nuevo_texto = label_res.cget("text") + boton.cget("text")
        label_res.config(text=nuevo_texto)
        return

boton0.config(command=lambda: agregar_texto(boton0))
boton1.config(command=lambda: agregar_texto(boton1))
boton2.config(command=lambda: agregar_texto(boton2))
boton3.config(command=lambda: agregar_texto(boton3))
boton4.config(command=lambda: agregar_texto(boton4))
boton5.config(command=lambda: agregar_texto(boton5))
boton6.config(command=lambda: agregar_texto(boton6))
boton7.config(command=lambda: agregar_texto(boton7))
boton8.config(command=lambda: agregar_texto(boton8))
boton9.config(command=lambda: agregar_texto(boton9))

boton0.place(x = 88, y = 512)
boton1.place(x = 0, y = 424)
boton2.place(x = 88, y = 424)
boton3.place(x = 176, y = 424)
boton4.place(x = 0, y = 336)
boton5.place(x = 88, y = 336)
boton6.place(x = 176, y = 336)
boton7.place(x = 0, y = 248)
boton8.place(x = 88, y = 248)
boton9.place(x = 176, y = 248)
boton_punto.place(x = 176, y = 512)
boton_signo.place(x = 0, y = 512)
boton_mas.place(x = 264, y = 160)
boton_menos.place(x = 264, y = 248)
boton_mult.place(x = 264, y = 336)
boton_div.place(x = 264, y = 424)
boton_igual.place(x = 264, y = 512)
boton_back.place(x = 0, y = 160)
boton_c.place(x = 88, y = 160)
boton_ce.place(x = 176, y = 160)

def act_op(operacion):
    statement = label_op.cget("text")
    statement2 = ""
    statement2 += " " + label_res.cget("text") + " " + operacion
    statement += statement2
    label_op.config(text= statement)
    return

def type_op(boton):
    operacion = boton.cget("text")
    act_op(operacion)
    label_res.config(text="0")
    return

def borrar():
    label_res.config(text="0")
    return

def borrar_todo():
    label_res.config(text="0")
    label_op.config(text="")
    return

def resultado():
    global lock
    if("=" in label_op.cget("text")):
        return
    else:
        operacion = label_op.cget("text") + " " + label_res.cget("text")
        label_op.config(text= operacion + " =")
        try:
            var_resultado = str(eval(operacion))
            label_res.config(text=var_resultado)
            lock = True
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero")
            label_op.config(text="")
            label_res.config(text="0")
            return
        except SyntaxError:
            messagebox.showerror("Error", "Error de Sintáxis")
            label_res.config(text="0")
            label_op.config(text="")
            return
        return
    
def punto():
    if("." in label_res.cget("text")):
        return
    else:
        texto_punto = label_res.cget("text") + "."
        label_res.config(text=texto_punto)
        return

def signo():
    try:
        num_signo = int(label_res.cget("text"))*-1
        label_res.config(text=str(num_signo))
    except ValueError:
        try:
            num_signo = float(label_res.cget("text"))*-1
            label_res.config(text=str(num_signo))    
        except ValueError:
            messagebox.showerror("Error", "Error de Sintáxis")
            label_res.config(text="0")
            label_op.config(text="")
            return

def backspace():
    global lock
    if(lock):
        label_op.config(text="")
        lock = False
        return
    if(len(label_res.cget("text"))==1):
        label_res.config(text="0")
        return
    else:
        back = label_res.cget("text")
        back = back[:-1]
        label_res.config(text=back)
        return

boton_c.config(command=lambda:borrar_todo())
boton_ce.config(command=lambda:borrar())
boton_igual.config(command=lambda:resultado())
boton_mas.config(command=lambda:type_op(boton_mas))
boton_menos.config(command=lambda:type_op(boton_menos))
boton_mult.config(command=lambda:type_op(boton_mult))
boton_div.config(command=lambda:type_op(boton_div))
boton_punto.config(command=lambda:punto())
boton_signo.config(command=lambda:signo())
boton_back.config(command=lambda:backspace())

ventana.mainloop()