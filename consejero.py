from experta import *
import tkinter as tk
from tkinter import messagebox


class Meteo(Fact):
    """Información sobre el clima"""
    pass


class ConsejeroVestimentario(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.consejos = []

    # Ejemplo de combinaciones con diferentes niveles de temperatura, humedad, uv, viento, sol y precipitación.

 # Clima frío (0-15°C), baja humedad, bajo UV, viento en calma, soleado, sin precipitación
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv <= 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=0))  # Sin precipitación
    def frio_baja_humedad_sin_lluvia(self):
        self.consejos.append("Clima frío, soleado y seco. Usa ropa abrigada ligera, sin necesidad de impermeable.")

    # Clima frío (0-15°C), baja humedad, bajo UV, viento moderado, nublado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv <= 1)),
          Meteo(viento=P(lambda viento: viento > 0 and viento <= 10)),
          Meteo(sol=2),  # Nublado
          Meteo(precip=1))  # Lluvia
    def frio_baja_humedad_lluvia_nublado(self):
        self.consejos.append("Clima frío, nublado y lluvioso. Usa un abrigo impermeable y suéter grueso.")

    # Clima templado (16-25°C), alta humedad, medio UV, viento fuerte, soleado, sin precipitación
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv > 1 and uv <= 5)),
          Meteo(viento=P(lambda viento: viento > 10)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=0))  # Sin precipitación
    def templado_alta_humedad_sin_lluvia_viento_fuerte(self):
        self.consejos.append("Clima templado con alta humedad y viento fuerte. Usa ropa ligera, pero protege tu cara del viento.")

    # Clima muy cálido (26-35°C), baja humedad, alto UV, viento moderado, soleado, sin precipitación
    @Rule(Meteo(temp=P(lambda temp: temp > 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv > 5)),
          Meteo(viento=P(lambda viento: viento > 0 and viento <= 10)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=0))  # Sin precipitación
    def muy_calido_baja_humedad_uv_alto(self):
        self.consejos.append("Clima muy cálido, UV alto y sin precipitación. Usa protector solar, ropa ligera y gafas de sol.")
    
    # Clima frío (0-15°C), baja humedad, bajo UV, viento en calma, soleado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv <= 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=1))  # Lluvia
    def frio_baja_humedad_lluvia(self):
        self.consejos.append("Hace frío con baja humedad y lluvia. Usa un impermeable ligero y suéter.")

    # Clima frío (0-15°C), baja humedad, bajo UV, viento en calma, nublado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv <= 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2),  # Nublado
          Meteo(precip=1))  # Lluvia
    def frio_baja_humedad_lluvia_nublado(self):
        self.consejos.append("Hace frío con baja humedad, nublado y con lluvia. Usa un impermeable ligero y una bufanda.")

    # Clima frío (0-15°C), baja humedad, bajo UV, viento moderado, soleado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv <= 1)),
          Meteo(viento=P(lambda viento: viento > 0 and viento <= 10)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=1))  # Lluvia
    def frio_baja_humedad_lluvia_viento_moderado(self):
        self.consejos.append("Hace frío, con lluvia y viento moderado. Usa una chaqueta impermeable y suéter grueso.")

    # Clima frío (0-15°C), baja humedad, bajo UV, viento fuerte, soleado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv <= 1)),
          Meteo(viento=P(lambda viento: viento > 10)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=1))  # Lluvia
    def frio_baja_humedad_lluvia_viento_fuerte(self):
        self.consejos.append("Hace frío con viento fuerte y lluvia. Usa un abrigo impermeable y bufanda gruesa.")

    # Clima frío (0-15°C), alta humedad, bajo UV, viento fuerte, soleado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv <= 1)),
          Meteo(viento=P(lambda viento: viento > 10)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=1))  # Lluvia
    def frio_alta_humedad_lluvia_viento_fuerte(self):
        self.consejos.append("Hace frío con lluvia, viento fuerte y alta humedad. Usa ropa térmica e impermeable.")

    # Clima templado (16-25°C), baja humedad, medio UV, viento en calma, soleado, sin precipitación
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv > 1 and uv <= 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=0))  # Sin precipitación
    def templado_baja_humedad_sin_lluvia(self):
        self.consejos.append("Clima templado con baja humedad y sin lluvia. Usa ropa ligera y una gorra.")

    # Clima templado (16-25°C), alta humedad, medio UV, viento moderado, soleado, sin precipitación
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv > 1 and uv <= 5)),
          Meteo(viento=P(lambda viento: viento > 0 and viento <= 10)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=0))  # Sin precipitación
    def templado_alta_humedad_sin_lluvia(self):
        self.consejos.append("Clima templado con alta humedad y sin lluvia. Usa ropa ligera y ventilada.")

    # Clima muy cálido (26-35°C), alta humedad, alto UV, viento en calma, soleado, sin precipitación
    @Rule(Meteo(temp=P(lambda temp: temp > 25)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv > 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=0))  # Sin precipitación
    def muy_calido_alta_humedad_sin_lluvia(self):
        self.consejos.append("Clima muy cálido, alta humedad y sin lluvia. Usa ropa ligera, protector solar y mantente hidratado.")

    # Clima muy cálido (26-35°C), baja humedad, alto UV, viento fuerte, soleado, sin precipitación
    @Rule(Meteo(temp=P(lambda temp: temp > 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv > 5)),
          Meteo(viento=P(lambda viento: viento > 10)),
          Meteo(sol=1),  # Soleado
          Meteo(precip=0))  # Sin precipitación
    def muy_calido_baja_humedad_viento_fuerte(self):
        self.consejos.append("Clima muy cálido con viento fuerte y baja humedad. Usa ropa ligera, protector solar y gafas.")

    # Método para mostrar el consejo
    def mostrar_consejo(self):
        if not self.consejos:
            self.consejos.append("No hay una recomendación específica para esta combinación.")
        consejo_final = "\n".join(self.consejos)
        messagebox.showinfo("Consejo Vestimentario", consejo_final)

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Consejero Vestimentario")

# Definir el tamaño de la ventana
width = 400
height = 500
root.geometry(f"{width}x{height}")

# Obtener las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la posición x e y para centrar la ventana
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

# Posicionar la ventana en el centro de la pantalla
root.geometry(f'+{x}+{y}')

# Variables para los botones de opción
temp_var = tk.IntVar()
humedad_var = tk.IntVar()
uv_var = tk.IntVar()
viento_var = tk.IntVar()
sol_var = tk.IntVar()  # 1: Soleado, 2: Nublado
precip_var = tk.IntVar()  # 1: Lluvia, 2: Nieve


# Función llamada cuando el usuario envía sus elecciones
def enviar_opciones():
    temp = temp_var.get()
    humedad = humedad_var.get()
    uv = uv_var.get()
    viento = viento_var.get()
    sol = sol_var.get()
    precip = precip_var.get()
    
    # Ejecutar motor
    consejero = ConsejeroVestimentario()
    consejero.reset()

    consejero.declare(Meteo(temp=temp, humedad=humedad, uv=uv, viento=viento, sol=sol, precip=precip))
    consejero.run()
    consejero.mostrar_consejo()


# Widgets para la temperatura
tk.Label(root, text="Temperatura:").pack()
tk.Radiobutton(root, text="0-15", variable=temp_var, value=0).pack()
tk.Radiobutton(root, text="16-25", variable=temp_var, value=16).pack()
tk.Radiobutton(root, text="26-35", variable=temp_var, value=26).pack()

# Widgets para la humedad
tk.Label(root, text="Humedad:").pack()
tk.Radiobutton(root, text="0-30", variable=humedad_var, value=30).pack()
tk.Radiobutton(root, text="31-60", variable=humedad_var, value=60).pack()

# Widgets para el índice UV
tk.Label(root, text="Índice UV:").pack()
tk.Radiobutton(root, text="Bajo", variable=uv_var, value=1).pack()
tk.Radiobutton(root, text="Medio", variable=uv_var, value=5).pack()

# Widgets para el viento
tk.Label(root, text="Viento:").pack()
tk.Radiobutton(root, text="Calma", variable=viento_var, value=0).pack()
tk.Radiobutton(root, text="Moderado", variable=viento_var, value=10).pack()
tk.Radiobutton(root, text="Extremo", variable=viento_var, value=20).pack()

# Widgets para sol y nubes
tk.Label(root, text="Condiciones de sol:").pack()
tk.Radiobutton(root, text="Soleado", variable=sol_var, value=1).pack()
tk.Radiobutton(root, text="Nublado", variable=sol_var, value=2).pack()

# Widgets para precipitaciones
tk.Label(root, text="Precipitaciones:").pack()
tk.Radiobutton(root, text="Lluvia", variable=precip_var, value=1).pack()
tk.Radiobutton(root, text="Nieve", variable=precip_var, value=2).pack()

# Botón de envío
submit_button = tk.Button(root, text="Enviar", command=enviar_opciones)
submit_button.pack()

# Ejecutar la aplicación Tkinter
root.mainloop()