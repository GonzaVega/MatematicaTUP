# Primera iteración con AI, SIN interfaz gráfica.
# def mostrar_menu():
#     print("\nSeleccione una operación lógica:")
#     print("1. AND")
#     print("2. OR")
#     print("3. NOT")
#     print("4. XOR")
#     print("Q. Salir")
#     return input("Ingrese el número de la operación o 'Q' para salir: ").strip().lower()

# def generar_tabla_binaria(nombre, operador):
#     print(f"\nTabla de verdad - {nombre}")
#     print("A | B | Resultado")
#     for A in [0, 1]:
#         for B in [0, 1]:
#             resultado = operador(A, B)
#             print(f"{A} | {B} |    {resultado}")

# def generar_tabla_unaria(nombre, operador):
#     print(f"\nTabla de verdad - {nombre}")
#     print("A | Resultado")
#     for A in [0, 1]:
#         resultado = operador(A)
#         print(f"{A} |   {resultado}")

# def main():
#     while True:
#         opcion = mostrar_menu()

#         if opcion == "1":
#             generar_tabla_binaria("AND", lambda a, b: a & b)
#         elif opcion == "2":
#             generar_tabla_binaria("OR", lambda a, b: a | b)
#         elif opcion == "3":
#             generar_tabla_unaria("NOT", lambda a: int(not a))
#         elif opcion == "4":
#             generar_tabla_binaria("XOR", lambda a, b: a ^ b)
#         elif opcion == "q":
#             print("¡Gracias por usar el sistema!")
#             break
#         else:
#             print("Opción no válida. Intente nuevamente.")

# if __name__ == "__main__":
#     main()

# Segunda iteración con AI, CON interfaz gráfica.

# import tkinter as tk
# from tkinter import ttk

# def generar_tabla(operacion):
#     resultados = []
#     if operacion == "NOT":
#         resultados.append(("A", "Resultado"))
#         for A in [0, 1]:
#             resultados.append((A, int(not A)))
#     else:
#         resultados.append(("A", "B", "Resultado"))
#         for A in [0, 1]:
#             for B in [0, 1]:
#                 if operacion == "AND":
#                     res = A & B
#                 elif operacion == "OR":
#                     res = A | B
#                 elif operacion == "XOR":
#                     res = A ^ B
#                 resultados.append((A, B, res))
#     return resultados

# def mostrar_tabla(operacion):
#     for widget in tabla_frame.winfo_children():
#         widget.destroy()

#     tabla = generar_tabla(operacion)
#     for i, fila in enumerate(tabla):
#         for j, valor in enumerate(fila):
#             lbl = ttk.Label(tabla_frame, text=str(valor), padding=5)
#             lbl.grid(row=i, column=j, padx=5, pady=5)

# # Interfaz principal
# root = tk.Tk()
# root.title("Tablas de Verdad - Álgebra de Boole")

# ttk.Label(root, text="Seleccione una operación lógica:", padding=10).pack()

# frame_botones = ttk.Frame(root)
# frame_botones.pack()

# for op in ["AND", "OR", "NOT", "XOR"]:
#     btn = ttk.Button(frame_botones, text=op, command=lambda op=op: mostrar_tabla(op))
#     btn.pack(side="left", padx=5)

# tabla_frame = ttk.Frame(root)
# tabla_frame.pack(pady=20)

# ttk.Button(root, text="Salir", command=root.quit).pack(pady=10)

# root.mainloop()

# Tercera iteración con AI, CON interfaz gráfica.
# import tkinter as tk
# from tkinter import ttk

# def generar_tabla(operacion):
#     resultados = []
#     if operacion == "NOT":
#         resultados.append(("A", "Resultado"))
#         for A in [0, 1]:
#             resultados.append((A, int(not A)))
#     else:
#         resultados.append(("A", "B", "Resultado"))
#         for A in [0, 1]:
#             for B in [0, 1]:
#                 if operacion == "AND":
#                     res = A & B
#                 elif operacion == "OR":
#                     res = A | B
#                 elif operacion == "XOR":
#                     res = A ^ B
#                 resultados.append((A, B, res))
#     return resultados

# def mostrar_tabla(operacion):
#     # Limpiar contenido anterior
#     for widget in tabla_frame.winfo_children():
#         widget.destroy()
#     canvas.delete("all")

#     # Mostrar tabla
#     tabla = generar_tabla(operacion)
#     for i, fila in enumerate(tabla):
#         for j, valor in enumerate(fila):
#             lbl = ttk.Label(tabla_frame, text=str(valor), padding=5)
#             lbl.grid(row=i, column=j, padx=5, pady=5)

#     # Mostrar representación gráfica
#     if operacion == "AND":
#         dibujar_and()
#     elif operacion == "OR":
#         dibujar_or()
#     elif operacion == "NOT":
#         dibujar_not()
#     elif operacion == "XOR":
#         dibujar_xor()

# # ===== Dibujos de circuitos =====

# def dibujar_and():
#     canvas.create_text(100, 20, text="Circuito: AND", font=("Arial", 12, "bold"))
#     canvas.create_line(10, 60, 50, 60)   # Entrada A
#     canvas.create_line(10, 100, 50, 100) # Entrada B
#     canvas.create_rectangle(50, 50, 100, 110, outline="black")  # caja
#     canvas.create_arc(75, 50, 125, 110, start=270, extent=180, style=tk.ARC)
#     canvas.create_line(125, 80, 170, 80)  # salida

# def dibujar_or():
#     canvas.create_text(100, 20, text="Circuito: OR", font=("Arial", 12, "bold"))
#     canvas.create_line(10, 60, 50, 60)
#     canvas.create_line(10, 100, 50, 100)
#     canvas.create_arc(40, 30, 100, 130, start=270, extent=180, style=tk.ARC)
#     canvas.create_arc(20, 40, 120, 120, start=270, extent=180, style=tk.ARC)
#     canvas.create_line(120, 80, 170, 80)

# def dibujar_not():
#     canvas.create_text(100, 20, text="Circuito: NOT", font=("Arial", 12, "bold"))
#     canvas.create_line(10, 80, 50, 80)
#     canvas.create_polygon(50, 60, 100, 80, 50, 100, outline="black", fill="")
#     canvas.create_oval(100, 75, 110, 85, outline="black")
#     canvas.create_line(110, 80, 150, 80)

# def dibujar_xor():
#     canvas.create_text(100, 20, text="Circuito: XOR", font=("Arial", 12, "bold"))
#     canvas.create_line(10, 60, 50, 60)
#     canvas.create_line(10, 100, 50, 100)
#     canvas.create_arc(40, 30, 100, 130, start=270, extent=180, style=tk.ARC)
#     canvas.create_arc(25, 40, 105, 120, start=270, extent=180, style=tk.ARC)
#     canvas.create_line(120, 80, 170, 80)

# # ===== Interfaz principal =====

# root = tk.Tk()
# root.title("Tablas de Verdad - Álgebra de Boole")

# ttk.Label(root, text="Seleccione una operación lógica:", padding=10).pack()

# frame_botones = ttk.Frame(root)
# frame_botones.pack()

# for op in ["AND", "OR", "NOT", "XOR"]:
#     btn = ttk.Button(frame_botones, text=op, command=lambda op=op: mostrar_tabla(op))
#     btn.pack(side="left", padx=5)

# tabla_frame = ttk.Frame(root)
# tabla_frame.pack(pady=10)

# canvas = tk.Canvas(root, width=200, height=150, bg="white")
# canvas.pack(pady=10)

# ttk.Button(root, text="Salir", command=root.quit).pack(pady=10)

# root.mainloop()

# Cuarta iteración con AI, CON interfaz gráfica y corrección de errores.

# import tkinter as tk
# from tkinter import ttk, messagebox

# def generar_tabla(operacion):
#     resultados = []
#     if operacion == "NOT":
#         resultados.append(("A", "Resultado"))
#         for A in [0, 1]:
#             resultados.append((A, int(not A)))
#     else:
#         resultados.append(("A", "B", "Resultado"))
#         for A in [0, 1]:
#             for B in [0, 1]:
#                 if operacion == "AND":
#                     res = A & B
#                 elif operacion == "OR":
#                     res = A | B
#                 elif operacion == "XOR":
#                     res = A ^ B
#                 resultados.append((A, B, res))
#     return resultados

# def mostrar_tabla(operacion):
#     # Limpiar contenido anterior
#     for widget in tabla_frame.winfo_children():
#         widget.destroy()
#     canvas.delete("all")

#     # Mostrar tabla
#     tabla = generar_tabla(operacion)
#     for i, fila in enumerate(tabla):
#         for j, valor in enumerate(fila):
#             lbl = ttk.Label(tabla_frame, text=str(valor), padding=5)
#             lbl.grid(row=i, column=j, padx=5, pady=5)

#     # Mostrar representación gráfica
#     if operacion == "AND":
#         dibujar_and()
#     elif operacion == "OR":
#         dibujar_or()
#     elif operacion == "NOT":
#         dibujar_not()
#     elif operacion == "XOR":
#         dibujar_xor()

# # ===== Dibujos de circuitos =====

# def dibujar_and():
#     canvas.create_text(100, 20, text="Circuito: AND", font=("Arial", 12, "bold"))
#     canvas.create_line(10, 60, 50, 60)   # Entrada A
#     canvas.create_line(10, 100, 50, 100) # Entrada B
#     canvas.create_rectangle(50, 50, 100, 110, outline="black")  # Caja rectangular
#     canvas.create_arc(75, 50, 125, 110, start=270, extent=180, style=tk.ARC)
#     canvas.create_line(125, 80, 170, 80)  # Salida

# # Modificado en una 5ta. y 6ta. iteración con AI.
# def dibujar_or():
#     canvas.create_text(100, 20, text="Circuito: OR", font=("Arial", 12, "bold"))
#     canvas.create_line(10, 60, 50, 60)
#     canvas.create_line(10, 100, 50, 100)
#     canvas.create_arc(40, 30, 120, 130, start=270, extent=180, style=tk.ARC)
#     canvas.create_arc(20, 50, 100, 110, start=270, extent=180, style=tk.ARC)
#     canvas.create_arc(95, 45, 145, 115, start=270, extent=180, style=tk.ARC)  # Curva de salida
#     canvas.create_line(145, 80, 180, 80)
    
# def dibujar_not():
#     canvas.create_text(100, 20, text="Circuito: NOT", font=("Arial", 12, "bold"))
#     canvas.create_line(10, 80, 50, 80)
#     canvas.create_polygon(50, 60, 100, 80, 50, 100, outline="black", fill="")
#     canvas.create_oval(100, 75, 110, 85, outline="black")
#     canvas.create_line(110, 80, 150, 80)

# def dibujar_xor():
#     canvas.create_text(100, 20, text="Circuito: XOR", font=("Arial", 12, "bold"))
#     canvas.create_line(10, 60, 50, 60)
#     canvas.create_line(10, 100, 50, 100)
#     canvas.create_arc(35, 30, 115, 130, start=270, extent=180, style=tk.ARC)
#     canvas.create_arc(15, 50, 95, 110, start=270, extent=180, style=tk.ARC)
#     canvas.create_arc(100, 45, 150, 115, start=270, extent=180, style=tk.ARC)  # Curva de salida
#     canvas.create_line(150, 80, 185, 80)
    
# # ===== Función de salida con mensaje =====

# def salir_con_mensaje():
#     messagebox.showinfo("¡Hasta pronto!", "Gracias por usar el sistema. ¡Hasta luego!")
#     root.destroy()

# # ===== Interfaz principal =====

# root = tk.Tk()
# root.title("Tablas de Verdad - Álgebra de Boole")

# ttk.Label(root, text="Seleccione una operación lógica:", padding=10).pack()

# frame_botones = ttk.Frame(root)
# frame_botones.pack()

# for op in ["AND", "OR", "NOT", "XOR"]:
#     btn = ttk.Button(frame_botones, text=op, command=lambda op=op: mostrar_tabla(op))
#     btn.pack(side="left", padx=5)

# tabla_frame = ttk.Frame(root)
# tabla_frame.pack(pady=10)

# canvas = tk.Canvas(root, width=250, height=160, bg="white")
# canvas.pack(pady=10)

# ttk.Button(root, text="Salir", command=salir_con_mensaje).pack(pady=10)

# root.mainloop()

# Sexta iteracion con AI, con imagenes en lugar de dibujos. Versión final.-

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Variables globales para las imágenes
imagen_and = None
imagen_or = None
imagen_not = None
imagen_xor = None

def generar_tabla(operacion):
  resultados = []
  if operacion == "NOT":
    resultados.append(("A", "Resultado"))
    for A in [0, 1]:
      resultados.append((A, int(not A)))
  else:
    resultados.append(("A", "B", "Resultado"))
    for A in [0, 1]:
      for B in [0, 1]:
        if operacion == "AND":
          res = A & B
        elif operacion == "OR":
          res = A | B
        elif operacion == "XOR":
          res = A ^ B
        resultados.append((A, B, res))
  return resultados

def mostrar_tabla(operacion):
  # Limpiar contenido anterior
  for widget in tabla_frame.winfo_children():
        widget.destroy()
  canvas.delete("all")

  # Mostrar tabla
  tabla = generar_tabla(operacion)
  for i, fila in enumerate(tabla):
    for j, valor in enumerate(fila):
      lbl = ttk.Label(tabla_frame, text=str(valor), padding=5)
      lbl.grid(row=i, column=j, padx=5, pady=5)

  # Mostrar representación gráfica (imagen)
  if operacion == "AND":
    dibujar_and()
  elif operacion == "OR":
    dibujar_or()
  elif operacion == "NOT":
    dibujar_not()
  elif operacion == "XOR":
    dibujar_xor()

# ===== Dibujos (con imágenes) de circuitos =====

# De la interacción con los modelos de IA se advierte que podemos refactorizar las rutas y el contructor de imágenes.

def contructor_imagen_tk (nombre_archivo):
  ruta_directorio_script = os.path.dirname(os.path.abspath(__file__))
  ruta_imagen = os.path.join(ruta_directorio_script, "imagenes", nombre_archivo)
  try:
    img = Image.open(ruta_imagen)
    img_resized = img.resize((150, 100), Image.BILINEAR)
    imagen_tk = ImageTk.PhotoImage(img_resized)
    return imagen_tk
  except FileNotFoundError:
    messagebox.showerror("Error", f"No se encontró la imagen: {ruta_imagen}")
  return None

def dibujar_and():
  global imagen_and
  canvas.create_text(125, 15, text="Circuito: AND", font=("Arial", 12, "bold"))
  imagen_and = contructor_imagen_tk("compuerta_and.png")
  if imagen_and:
    canvas.create_image(125, 90, image=imagen_and)
    
def dibujar_or():
  global imagen_or
  canvas.create_text(125, 15, text="Circuito: OR", font=("Arial", 12, "bold"))
  imagen_or = contructor_imagen_tk("compuerta_or.png")
  if imagen_or:
    canvas.create_image(125, 90, image=imagen_or)

def dibujar_not():
  global imagen_not
  canvas.create_text(125, 15, text="Circuito: NOT", font=("Arial", 12, "bold"))
  imagen_not = contructor_imagen_tk("compuerta_not.png")
  if imagen_not:
    canvas.create_image(125, 90, image=imagen_not)

def dibujar_xor():
  global imagen_xor
  canvas.create_text(125, 15, text="Circuito: XOR", font=("Arial", 12, "bold"))
  imagen_xor = contructor_imagen_tk("compuerta_xor.png")
  if imagen_xor:
    canvas.create_image(125, 90, image=imagen_xor)

# ===== Función de salida con mensaje =====

def salir_con_mensaje():
  messagebox.showinfo("¡Hasta pronto!", "Gracias por usar el sistema. ¡Hasta luego!")
  root.destroy()

# ===== Interfaz principal =====

root = tk.Tk()
root.title("Tablas de Verdad - Álgebra de Boole")

ttk.Label(root, text="Seleccione una operación lógica:", padding=10).pack()

frame_botones = ttk.Frame(root)
frame_botones.pack()

for op in ["AND", "OR", "NOT", "XOR"]:
    btn = ttk.Button(frame_botones, text=op, command=lambda op=op: mostrar_tabla(op))
    btn.pack(side="left", padx=5)

tabla_frame = ttk.Frame(root)
tabla_frame.pack(pady=10)

canvas = tk.Canvas(root, width=250, height=160, bg="white")
canvas.pack(pady=10)

ttk.Button(root, text="Salir", command=salir_con_mensaje).pack(pady=10)

root.mainloop()
