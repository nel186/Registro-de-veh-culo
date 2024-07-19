import tkinter as tk
from tkinter import messagebox, ttk
import csv
from datetime import datetime

# Archivo CSV para almacenar los datos
archivo_datos = 'registro_vehiculos.csv'

def registrar_entrada():
    placa = entrada_placa.get()
    nombre = entrada_nombre.get()
    cedula = entrada_cedula.get()
    if placa and nombre and cedula:
        with open(archivo_datos, mode='a', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([placa, nombre, cedula, 'Entrada', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
        messagebox.showinfo("Registro de Entrada", f'Vehículo con placa {placa}, nombre {nombre} y cédula {cedula} registrado como entrada.')
        limpiar_campos()
    else:
        messagebox.showwarning("Advertencia", "Ingrese una placa, nombre y cédula válidos.")

def registrar_salida():
    placa = entrada_placa.get()
    if placa:
        registros = []
        encontrado = False
        with open(archivo_datos, mode='r') as archivo:
            lector = csv.reader(archivo)
            registros = list(lector)

        with open(archivo_datos, mode='w', newline='') as archivo:
            escritor = csv.writer(archivo)
            for registro in registros:
                if registro[0] == placa and registro[3] == 'Entrada' and not encontrado:
                    escritor.writerow([placa, registro[1], registro[2], 'Salida', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
                    encontrado = True
                else:
                    escritor.writerow(registro)
        
        if encontrado:
            messagebox.showinfo("Registro de Salida", f'Vehículo con placa {placa} registrado como salida.')
            limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", f'No se encontró un registro de entrada para el vehículo con placa {placa}.')
    else:
        messagebox.showwarning("Advertencia", "Ingrese una placa válida.")

def mostrar_registros():
    try:
        with open(archivo_datos, mode='r') as archivo:
            lector = csv.reader(archivo)
            registros = list(lector)
        
        if registros:
            ventana_registros = tk.Toplevel(ventana)
            ventana_registros.title("Registros")
            ventana_registros.geometry("600x400")
            ventana_registros.configure(bg='#e0e0e0')
            texto_registros = tk.Text(ventana_registros, width=80, height=20)
            texto_registros.pack(pady=10)

            for i, fila in enumerate(registros):
                texto_registros.insert(tk.END, f'{i + 1}. Placa: {fila[0]}, Nombre: {fila[1]}, Cédula: {fila[2]}, Tipo: {fila[3]}, Fecha y Hora: {fila[4]}\n')

            tk.Label(ventana_registros, text="Ingrese el número del registro a modificar:", bg='#e0e0e0').pack(pady=5)
            entrada_numero = tk.Entry(ventana_registros)
            entrada_numero.pack(pady=5)
            
            def modificar_seleccionado():
                try:
                    numero = int(entrada_numero.get()) - 1
                    if 0 <= numero < len(registros):
                        registro = registros[numero]
                        ventana_modificar = tk.Toplevel(ventana_registros)
                        ventana_modificar.title("Modificar Registro")
                        ventana_modificar.geometry("400x300")
                        ventana_modificar.configure(bg='#e0e0e0')
                        
                        tk.Label(ventana_modificar, text="Nueva Placa:", bg='#e0e0e0').pack(pady=5)
                        nueva_placa = tk.Entry(ventana_modificar)
                        nueva_placa.pack(pady=5)
                        nueva_placa.insert(tk.END, registro[0])
                        
                        tk.Label(ventana_modificar, text="Nuevo Nombre:", bg='#e0e0e0').pack(pady=5)
                        nuevo_nombre = tk.Entry(ventana_modificar)
                        nuevo_nombre.pack(pady=5)
                        nuevo_nombre.insert(tk.END, registro[1])
                        
                        tk.Label(ventana_modificar, text="Nueva Cédula:", bg='#e0e0e0').pack(pady=5)
                        nueva_cedula = tk.Entry(ventana_modificar)
                        nueva_cedula.pack(pady=5)
                        nueva_cedula.insert(tk.END, registro[2])

                        def guardar_modificaciones():
                            if nueva_placa.get() and nuevo_nombre.get() and nueva_cedula.get():
                                registros[numero] = [nueva_placa.get(), nuevo_nombre.get(), nueva_cedula.get(), registro[3], registro[4]]
                                with open(archivo_datos, mode='w', newline='') as archivo:
                                    escritor = csv.writer(archivo)
                                    escritor.writerows(registros)
                                ventana_modificar.destroy()
                                ventana_registros.destroy()
                                messagebox.showinfo("Modificación", f'Registro modificado con éxito.')
                            else:
                                messagebox.showwarning("Advertencia", "Ingrese una placa, nombre y cédula válidos.")
                        
                        ttk.Button(ventana_modificar, text="Guardar Cambios", command=guardar_modificaciones).pack(pady=10)
                        
                        ttk.Button(ventana_modificar, text="Eliminar Registro", command=lambda: eliminar_registro(numero)).pack(pady=10)
                    else:
                        messagebox.showwarning("Advertencia", "Número de registro no válido.")
                except ValueError:
                    messagebox.showwarning("Advertencia", "Ingrese un número válido.")
                
            def eliminar_registro(index):
                registros.pop(index)
                with open(archivo_datos, mode='w', newline='') as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerows(registros)
                ventana_registros.destroy()
                messagebox.showinfo("Eliminación", f'Registro eliminado con éxito.')
                
            ttk.Button(ventana_registros, text="Modificar Registro", command=modificar_seleccionado).pack(pady=10)
        else:
            messagebox.showinfo("Registros", "No hay registros disponibles.")
    except FileNotFoundError:
        messagebox.showinfo("Registros", "No hay registros disponibles.")

def limpiar_campos():
    entrada_placa.delete(0, tk.END)
    entrada_nombre.delete(0, tk.END)
    entrada_cedula.delete(0, tk.END)

def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Este es un sistema básico para el registro de entrada y salida de vehículos en un parqueadero.\n\n"
                                 "Para registrar una entrada, ingrese la placa, nombre del conductor y cédula, luego presione 'Registrar Entrada'.\n"
                                 "Para registrar una salida, ingrese la placa del vehículo y presione 'Registrar Salida'.\n"
                                 "Para ver y modificar registros, presione 'Mostrar Registros'.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Vehículos")
ventana.geometry("600x400")  # Configuración inicial del tamaño de la ventana
ventana.state('zoomed')  # Maximiza la ventana al iniciar
ventana.configure(bg='#e0e0e0')

# Crear menú
menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)

# Añadir menú de ayuda
menu_ayuda = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Cómo utilizar", command=mostrar_ayuda)

# Crear widgets
tk.Label(ventana, text="Ingrese la placa del vehículo:", bg='#e0e0e0').pack(pady=10)
entrada_placa = tk.Entry(ventana)
entrada_placa.pack(pady=5)

tk.Label(ventana, text="Ingrese el nombre del conductor:", bg='#e0e0e0').pack(pady=10)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="Ingrese la cédula del conductor:", bg='#e0e0e0').pack(pady=10)
entrada_cedula = tk.Entry(ventana)
entrada_cedula.pack(pady=5)

ttk.Button(ventana, text="Registrar Entrada", command=registrar_entrada).pack(pady=5)
ttk.Button(ventana, text="Registrar Salida", command=registrar_salida).pack(pady=5)
ttk.Button(ventana, text="Mostrar Registros", command=mostrar_registros).pack(pady=5)
ttk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
