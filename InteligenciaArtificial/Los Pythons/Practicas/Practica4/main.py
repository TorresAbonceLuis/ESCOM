import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def setup_fuzzy_system():
    # Variables de entrada
    tipo_tela = ctrl.Antecedent(np.arange(0, 11, 1), 'tipo_tela')
    cantidad_ropa = ctrl.Antecedent(np.arange(0, 11, 1), 'cantidad_ropa')
    grado_suciedad = ctrl.Antecedent(np.arange(0, 11, 1), 'grado_suciedad')

    # Variables de salida
    cantidad_agua = ctrl.Consequent(np.arange(0, 101, 1), 'cantidad_agua')
    temperatura_agua = ctrl.Consequent(np.arange(0, 101, 1), 'temperatura_agua')
    tiempo_lavado = ctrl.Consequent(np.arange(0, 121, 1), 'tiempo_lavado')
    detergente = ctrl.Consequent(np.arange(0, 101, 1), 'detergente')

    # Funciones de membresía
    tipo_tela.automf(3, names=['delicada', 'normal', 'resistente'])
    cantidad_ropa.automf(3, names=['poca', 'media', 'mucha'])
    grado_suciedad.automf(3, names=['ligera', 'media', 'pesada'])

    cantidad_agua.automf(3, names=['poca', 'media', 'mucha'])
    temperatura_agua.automf(3, names=['fría', 'tibia', 'caliente'])
    tiempo_lavado.automf(3, names=['corto', 'medio', 'largo'])
    detergente.automf(3, names=['poco', 'medio', 'mucho'])

    # Reglas de inferencia
    regla1 = ctrl.Rule(tipo_tela['resistente'] & grado_suciedad['pesada'], 
                        [detergente['mucho'], tiempo_lavado['largo'], temperatura_agua['caliente'], cantidad_agua['mucha']])
    regla2 = ctrl.Rule(tipo_tela['delicada'] & grado_suciedad['ligera'],
                        [detergente['poco'], tiempo_lavado['corto'], temperatura_agua['fría'], cantidad_agua['poca']])
    regla3 = ctrl.Rule(cantidad_ropa['mucha'] & grado_suciedad['media'], 
                        [detergente['medio'], tiempo_lavado['medio'], temperatura_agua['tibia'], cantidad_agua['media']])
    regla4 = ctrl.Rule(tipo_tela['normal'] & cantidad_ropa['poca'] & grado_suciedad['ligera'], 
                        [detergente['poco'], tiempo_lavado['corto'], temperatura_agua['fría'], cantidad_agua['poca']])
    regla5 = ctrl.Rule(tipo_tela['delicada'] & cantidad_ropa['mucha'] & grado_suciedad['pesada'], 
                        [detergente['mucho'], tiempo_lavado['largo'], temperatura_agua['caliente'], cantidad_agua['mucha']])
    regla6 = ctrl.Rule(tipo_tela['normal'] & cantidad_ropa['mucha'] & grado_suciedad['ligera'], 
                        [detergente['medio'], tiempo_lavado['medio'], temperatura_agua['tibia'], cantidad_agua['media']])
    regla7 = ctrl.Rule(tipo_tela['resistente'] & cantidad_ropa['mucha'] & grado_suciedad['pesada'], 
                        [detergente['mucho'], tiempo_lavado['largo'], temperatura_agua['caliente'], cantidad_agua['mucha']])
    regla8 = ctrl.Rule(tipo_tela['resistente'] & cantidad_ropa['poca'] & grado_suciedad['media'], 
                        [detergente['medio'], tiempo_lavado['medio'], temperatura_agua['tibia'], cantidad_agua['media']])
    regla9 = ctrl.Rule(tipo_tela['delicada'] & cantidad_ropa['poca'] & grado_suciedad['ligera'], 
                        [detergente['poco'], tiempo_lavado['corto'], temperatura_agua['fría'], cantidad_agua['poca']])

    # Añadir reglas adicionales para cubrir más combinaciones
    regla10 = ctrl.Rule(tipo_tela['normal'] & grado_suciedad['media'],
                        [detergente['medio'], tiempo_lavado['medio'], temperatura_agua['tibia'], cantidad_agua['media']])
    regla11 = ctrl.Rule(tipo_tela['resistente'] & grado_suciedad['ligera'],
                        [detergente['poco'], tiempo_lavado['corto'], temperatura_agua['fría'], cantidad_agua['poca']])
    regla12 = ctrl.Rule(tipo_tela['delicada'] & cantidad_ropa['media'],
                        [detergente['medio'], tiempo_lavado['medio'], temperatura_agua['tibia'], cantidad_agua['media']])
    regla13 = ctrl.Rule(tipo_tela['normal'] & cantidad_ropa['media'] & grado_suciedad['pesada'],
                        [detergente['mucho'], tiempo_lavado['largo'], temperatura_agua['caliente'], cantidad_agua['mucha']])

    # Sistema de control
    control_system = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10, regla11, regla12, regla13])
    return ctrl.ControlSystemSimulation(control_system)

def setup_gui(washing_machine):
    window = tk.Tk()
    window.title("Sistema de Control para Lavado de Ropa")
    center_window(window, 400, 300)

    tipo_tela_var = tk.IntVar(value=5)
    cantidad_ropa_var = tk.IntVar(value=5)
    grado_suciedad_var = tk.IntVar(value=5)

    def calculate():
        washing_machine.input['tipo_tela'] = tipo_tela_var.get()
        washing_machine.input['cantidad_ropa'] = cantidad_ropa_var.get()
        washing_machine.input['grado_suciedad'] = grado_suciedad_var.get()
        washing_machine.compute()

        detergent_result.config(text=f"Detergente: {washing_machine.output['detergente']:.2f}")
        wash_time_result.config(text=f"Tiempo de Lavado: {washing_machine.output['tiempo_lavado']:.2f}")
        water_temp_result.config(text=f"Temperatura del Agua: {washing_machine.output['temperatura_agua']:.2f}")
        water_amount_result.config(text=f"Cantidad de Agua: {washing_machine.output['cantidad_agua']:.2f}")

    def regresar():
        window.destroy()
        setup_intro_window()

    return_button = ttk.Button(window, text="Regresar", command=regresar)
    return_button.pack(anchor='ne', padx=10, pady=5)

    ttk.Label(window, text="Tipo de Tela (0-Delicada, 10-Resistente):").pack()
    ttk.Scale(window, from_=0, to=10, orient='horizontal', variable=tipo_tela_var).pack()
    ttk.Label(window, text="Cantidad de Ropa (0-Poca, 10-Mucha):").pack()
    ttk.Scale(window, from_=0, to=10, orient='horizontal', variable=cantidad_ropa_var).pack()
    ttk.Label(window, text="Grado de Suciedad (0-Ligera, 10-Pesada):").pack()
    ttk.Scale(window, from_=0, to=10, orient='horizontal', variable=grado_suciedad_var).pack()

    ttk.Button(window, text="Calcular", command=calculate).pack()

    detergent_result = ttk.Label(window, text="Detergente: 0")
    detergent_result.pack()
    wash_time_result = ttk.Label(window, text="Tiempo de Lavado: 0")
    wash_time_result.pack()
    water_temp_result = ttk.Label(window, text="Temperatura del Agua: 0")
    water_temp_result.pack()
    water_amount_result = ttk.Label(window, text="Cantidad de Agua: 0")
    water_amount_result.pack()

    window.mainloop()

def setup_intro_window():
    intro_window = tk.Tk()
    intro_window.title("Inicio")
    center_window(intro_window, 500, 500)

    # Agregar logos
    logo_izquierda = Image.open("logo1.png")
    logo_derecha = Image.open("logo2.png")
    logo_enmedio = Image.open("logo3.png")

    # Cambiar el tamaño de las imágenes
    logo_izquierda = logo_izquierda.resize((120, 100))
    logo_derecha = logo_derecha.resize((120, 100))
    logo_enmedio = logo_enmedio.resize((120, 100))

    # Crear PhotoImage a partir de las imágenes redimensionadas
    logo_izquierda = ImageTk.PhotoImage(logo_izquierda)
    logo_derecha = ImageTk.PhotoImage(logo_derecha)
    logo_enmedio = ImageTk.PhotoImage(logo_enmedio)

    # Colocar los logotipos
    label_logo_izquierda = ttk.Label(intro_window, image=logo_izquierda)
    label_logo_izquierda.place(x=0, y=0)

    label_logo_enmedio = ttk.Label(intro_window, image=logo_enmedio)
    label_logo_enmedio.place(x=200, y=0)

    label_logo_derecha = ttk.Label(intro_window, image=logo_derecha)
    label_logo_derecha.place(x=380, y=0)

    # Información
    info_label = ttk.Label(intro_window, text="Instituto Politécnico Nacional\nEscuela Superior de Computo\n          Lavadora Difusa\n", font=("Times New Roman", 17))
    info_label.place(x=120, y=180)

    # Botones
    btn_inicio = ttk.Button(intro_window, text="Inicio", command=lambda: [intro_window.destroy(), setup_gui(washing_machine)])
    btn_inicio.place(x=200, y=350)
    btn_ayuda = tk.Button(intro_window, text="Ayuda", command=lambda: show_help_window(intro_window), fg='white', bg='red')
    btn_ayuda.place(x=215, y=375)

    intro_window.mainloop()

def show_help_window(intro_window):
    help_window = tk.Toplevel(intro_window)
    help_window.title("Ayuda")
    center_window(help_window, 450, 600)

    help_text = (
        "Este programa es un sistema de control difuso para una lavadora.\n\n"
        "Cómo funciona:\n"
        "1. Introduzca los valores de 'Tipo de Tela', 'Cantidad de Ropa' y 'Grado de Suciedad' "
        "utilizando las barras deslizantes.\n"
        "2. Haga clic en el botón 'Calcular' para obtener los valores calculados para "
        "'Detergente', 'Tiempo de Lavado', 'Temperatura del Agua' y 'Cantidad de Agua'.\n\n"
    )

    help_label = ttk.Label(help_window, text=help_text, font=("Times New Roman", 14), wraplength=400)
    help_label.pack(padx=20, pady=20)

    # Crear tabla con la información
    columns = ('Categoría', 'Descripción')
    data = [
        ('Tipo de Tela', 'Delicada, Normal, Resistente'),
        ('Cantidad de Ropa', 'Poca, Media, Mucha'),
        ('Grado de Suciedad', 'Ligera, Media, Pesada'),
        ('Cantidad de Agua', 'Poca, Media, Mucha'),
        ('Temperatura del Agua', 'Fría, Tibia, Caliente'),
        ('Tiempo de Lavado', 'Corto, Medio, Largo'),
        ('Detergente', 'Poco, Medio, Mucho')
    ]

    table_frame = ttk.Frame(help_window)
    table_frame.pack(padx=20, pady=20)

    table = ttk.Treeview(table_frame, columns=columns, show='headings', height=len(data))
    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor=tk.CENTER, width=150)

    for row in data:
        table.insert('', tk.END, values=row)

    table.pack()

    close_button = ttk.Button(help_window, text="Cerrar", command=help_window.destroy)
    close_button.pack(pady=10)

if __name__ == '__main__':
    washing_machine = setup_fuzzy_system()
    setup_intro_window()
