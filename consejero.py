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

    # Combinaciones simplificadas

    # 1. Clima frío (0-15°C), baja humedad (0-30), bajo UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def frio_baja_humedad_uv_bajo_viento_calma_despejado(self):
        self.consejos.append("Hace frío, con baja humedad y sin viento. Usa ropa abrigada ligera y gafas de sol, no se necesita impermeable.")

    # 2. Clima frío (0-15°C), baja humedad (0-30), bajo UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def frio_baja_humedad_uv_bajo_viento_calma_lluvia(self):
        self.consejos.append("Hace frío, con baja humedad y lluvia. Usa un impermeable ligero y ropa abrigada, no se necesita ropa pesada.")

    # 3. Clima frío (0-15°C), baja humedad (0-30), bajo UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def frio_baja_humedad_uv_bajo_viento_moderado_despejado(self):
        self.consejos.append("Hace frío con viento moderado. Usa una chaqueta cortavientos y gafas de sol, ideal para el clima seco.")

    # 4. Clima frío (0-15°C), baja humedad (0-30), bajo UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def frio_baja_humedad_uv_bajo_viento_moderado_lluvia(self):
        self.consejos.append("Hace frío con viento moderado y lluvia. Usa una chaqueta impermeable y bufanda ligera para protegerte del viento y la lluvia.")

    # 5. Clima frío (0-15°C), alta humedad (31-60), bajo UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def frio_alta_humedad_uv_bajo_viento_calma_despejado(self):
        self.consejos.append("Hace frío con alta humedad y sin viento. Usa ropa abrigada y gafas de sol, ideal para el clima seco pero con algo de humedad.")

    # 6. Clima frío (0-15°C), alta humedad (31-60), bajo UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def frio_alta_humedad_uv_bajo_viento_calma_lluvia(self):
        self.consejos.append("Hace frío con alta humedad y lluvia. Usa ropa térmica e impermeable, es recomendable llevar botas.")

    # 7. Clima frío (0-15°C), alta humedad (31-60), bajo UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def frio_alta_humedad_uv_bajo_viento_moderado_despejado(self):
        self.consejos.append("Hace frío, alta humedad y viento moderado. Usa ropa abrigada, un cortavientos y gafas de sol.")

    # 8. Clima frío (0-15°C), alta humedad (31-60), bajo UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: temp <= 15)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def frio_alta_humedad_uv_bajo_viento_moderado_lluvia(self):
        self.consejos.append("Hace frío, alta humedad, viento moderado y lluvia. Usa ropa térmica e impermeable y un cortavientos para protegerte del viento.")

    # 9. Clima templado (16-25°C), baja humedad (0-30), bajo UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def templado_baja_humedad_uv_bajo_viento_calma_despejado(self):
        self.consejos.append("Clima templado, baja humedad y sin viento. Usa ropa ligera y cómoda, no necesitas abrigo.")

    # 10. Clima templado (16-25°C), baja humedad (0-30), bajo UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def templado_baja_humedad_uv_bajo_viento_calma_lluvia(self):
        self.consejos.append("Clima templado con lluvia y baja humedad. Usa ropa ligera e impermeable, ideal para el clima húmedo.")

    # 11. Clima templado (16-25°C), baja humedad (0-30), bajo UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def templado_baja_humedad_uv_bajo_viento_moderado_despejado(self):
        self.consejos.append("Clima templado y seco, con viento moderado. Usa ropa ligera y cómoda, una chaqueta ligera por si acaso.")

    # 12. Clima templado (16-25°C), baja humedad (0-30), bajo UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def templado_baja_humedad_uv_bajo_viento_moderado_lluvia(self):
        self.consejos.append("Clima templado, con lluvia y viento moderado. Usa ropa ligera, impermeable y cortavientos para el viento y la lluvia.")

    # 13. Clima templado (16-25°C), baja humedad (0-30), medio UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def templado_baja_humedad_uv_medio_viento_calma_despejado(self):
        self.consejos.append("Clima templado con bajo viento y UV medio. Usa ropa ligera y protector solar, ideal para un día soleado.")

    # 14. Clima templado (16-25°C), baja humedad (0-30), medio UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def templado_baja_humedad_uv_medio_viento_calma_lluvia(self):
        self.consejos.append("Clima templado con lluvia y UV medio. Usa ropa ligera e impermeable, además de un paraguas para protegerte.")

    # 15. Clima templado (16-25°C), baja humedad (0-30), medio UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def templado_baja_humedad_uv_medio_viento_moderado_despejado(self):
        self.consejos.append("Clima templado con viento moderado y UV medio. Usa ropa ligera, protector solar, y una chaqueta ligera para el viento.")

    # 16. Clima templado (16-25°C), baja humedad (0-30), medio UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def templado_baja_humedad_uv_medio_viento_moderado_lluvia(self):
        self.consejos.append("Clima templado con viento moderado y lluvia. Usa ropa impermeable y un cortavientos, ideal para mantenerte seco y protegido.")

    # 17. Clima templado (16-25°C), alta humedad (31-60), medio UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def templado_alta_humedad_uv_medio_viento_calma_despejado(self):
        self.consejos.append("Clima templado y húmedo con UV medio. Usa ropa ligera y transpirable, y no olvides el protector solar.")

    # 18. Clima templado (16-25°C), alta humedad (31-60), medio UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def templado_alta_humedad_uv_medio_viento_calma_lluvia(self):
        self.consejos.append("Clima templado, con lluvia y alta humedad. Usa ropa ligera e impermeable, y trata de mantenerte fresco bajo la lluvia.")

    # 19. Clima templado (16-25°C), alta humedad (31-60), medio UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def templado_alta_humedad_uv_medio_viento_moderado_despejado(self):
        self.consejos.append("Clima templado con humedad alta y viento moderado. Usa ropa ligera, protector solar y una chaqueta ligera para el viento.")

    # 20. Clima templado (16-25°C), alta humedad (31-60), medio UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 16 <= temp <= 25)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def templado_alta_humedad_uv_medio_viento_moderado_lluvia(self):
        self.consejos.append("Clima templado con humedad alta, lluvia y viento moderado. Usa ropa ligera e impermeable, además de una chaqueta cortavientos.")

    # 21. Clima cálido (26-35°C), baja humedad (0-30), bajo UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def calido_baja_humedad_uv_bajo_viento_calma_despejado(self):
        self.consejos.append("Clima cálido y seco, sin viento. Usa ropa ligera, gafas de sol y protector solar para evitar quemaduras.")

    # 22. Clima cálido (26-35°C), baja humedad (0-30), bajo UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def calido_baja_humedad_uv_bajo_viento_calma_lluvia(self):
        self.consejos.append("Clima cálido, seco y con lluvia. Usa ropa ligera e impermeable, ideal para un día caluroso con lluvias ligeras.")

    # 23. Clima cálido (26-35°C), baja humedad (0-30), bajo UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def calido_baja_humedad_uv_bajo_viento_moderado_despejado(self):
        self.consejos.append("Clima cálido con viento moderado. Usa ropa ligera, gafas de sol y una chaqueta ligera para el viento.")

    # 24. Clima cálido (26-35°C), baja humedad (0-30), bajo UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 1)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def calido_baja_humedad_uv_bajo_viento_moderado_lluvia(self):
        self.consejos.append("Clima cálido con viento moderado y lluvia. Usa ropa ligera, impermeable y una chaqueta cortavientos para el viento y la lluvia.")
    
    # 25. Clima cálido (26-35°C), baja humedad (0-30), medio UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def calido_baja_humedad_uv_medio_viento_calma_despejado(self):
        self.consejos.append("Clima cálido con UV medio y sin viento. Usa ropa ligera, gafas de sol y protector solar para protegerte del sol.")

    # 26. Clima cálido (26-35°C), baja humedad (0-30), medio UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def calido_baja_humedad_uv_medio_viento_calma_lluvia(self):
        self.consejos.append("Clima cálido con UV medio y lluvia. Usa ropa ligera e impermeable, ideal para un día caluroso con lluvias.")

    # 27. Clima cálido (26-35°C), baja humedad (0-30), medio UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def calido_baja_humedad_uv_medio_viento_moderado_despejado(self):
        self.consejos.append("Clima cálido con UV medio y viento moderado. Usa ropa ligera, protector solar y una chaqueta ligera para el viento.")

    # 28. Clima cálido (26-35°C), baja humedad (0-30), medio UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def calido_baja_humedad_uv_medio_viento_moderado_lluvia(self):
        self.consejos.append("Clima cálido con UV medio, viento moderado y lluvia. Usa ropa ligera e impermeable, con chaqueta cortavientos para protegerte del viento y la lluvia.")

    # 29. Clima cálido (26-35°C), alta humedad (31-60), medio UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def calido_alta_humedad_uv_medio_viento_calma_despejado(self):
        self.consejos.append("Clima cálido con humedad alta y UV medio. Usa ropa transpirable y ligera, protector solar y gafas de sol.")

    # 30. Clima cálido (26-35°C), alta humedad (31-60), medio UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def calido_alta_humedad_uv_medio_viento_calma_lluvia(self):
        self.consejos.append("Clima cálido con humedad alta, UV medio y lluvia. Usa ropa ligera e impermeable, ideal para mantenerte fresco en la lluvia.")

    # 31. Clima cálido (26-35°C), alta humedad (31-60), medio UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def calido_alta_humedad_uv_medio_viento_moderado_despejado(self):
        self.consejos.append("Clima cálido con humedad alta y viento moderado. Usa ropa ligera, transpirable y protector solar para protegerte del sol.")

    # 32. Clima cálido (26-35°C), alta humedad (31-60), medio UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def calido_alta_humedad_uv_medio_viento_moderado_lluvia(self):
        self.consejos.append("Clima cálido con humedad alta, viento moderado y lluvia. Usa ropa ligera, impermeable y una chaqueta cortavientos para protegerte de la lluvia y el viento.")

    # 33. Clima cálido (26-35°C), baja humedad (0-30), alto UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def calido_baja_humedad_uv_alto_viento_calma_despejado(self):
        self.consejos.append("Clima cálido con UV alto y sin viento. Usa ropa ligera, protector solar, gafas de sol y mantente hidratado.")

    # 34. Clima cálido (26-35°C), baja humedad (0-30), alto UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def calido_baja_humedad_uv_alto_viento_calma_lluvia(self):
        self.consejos.append("Clima cálido con UV alto y lluvia. Usa ropa ligera, impermeable y protector solar, ideal para el clima caluroso y lluvioso.")

    # 35. Clima cálido (26-35°C), baja humedad (0-30), alto UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def calido_baja_humedad_uv_alto_viento_moderado_despejado(self):
        self.consejos.append("Clima cálido con UV alto y viento moderado. Usa ropa ligera, protector solar, gafas de sol y una chaqueta ligera para el viento.")

    # 36. Clima cálido (26-35°C), baja humedad (0-30), alto UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def calido_baja_humedad_uv_alto_viento_moderado_lluvia(self):
        self.consejos.append("Clima cálido con UV alto, viento moderado y lluvia. Usa ropa ligera, impermeable, protector solar y una chaqueta cortavientos para protegerte del viento y la lluvia.")

        # 37. Clima cálido (26-35°C), alta humedad (31-60), alto UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def calido_alta_humedad_uv_alto_viento_calma_despejado(self):
        self.consejos.append("Clima cálido con alta humedad y UV alto. Usa ropa ligera, protector solar, gafas de sol y mantente bien hidratado.")

    # 38. Clima cálido (26-35°C), alta humedad (31-60), alto UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def calido_alta_humedad_uv_alto_viento_calma_lluvia(self):
        self.consejos.append("Clima cálido con alta humedad, UV alto y lluvia. Usa ropa ligera e impermeable, protector solar, y trata de mantenerte fresco en la lluvia.")

    # 39. Clima cálido (26-35°C), alta humedad (31-60), alto UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def calido_alta_humedad_uv_alto_viento_moderado_despejado(self):
        self.consejos.append("Clima cálido con alta humedad, UV alto y viento moderado. Usa ropa ligera y transpirable, protector solar y una chaqueta ligera.")

    # 40. Clima cálido (26-35°C), alta humedad (31-60), alto UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def calido_alta_humedad_uv_alto_viento_moderado_lluvia(self):
        self.consejos.append("Clima cálido con alta humedad, viento moderado y lluvia. Usa ropa ligera e impermeable, con chaqueta cortavientos y protector solar.")

    # 41. Clima cálido (26-35°C), baja humedad (0-30), alto UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def calido_baja_humedad_uv_alto_viento_calma_despejado(self):
        self.consejos.append("Clima cálido y seco, con UV alto. Usa ropa ligera, gafas de sol, protector solar y mantente hidratado.")

    # 42. Clima cálido (26-35°C), baja humedad (0-30), alto UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def calido_baja_humedad_uv_alto_viento_calma_lluvia(self):
        self.consejos.append("Clima cálido y seco, con UV alto y lluvia. Usa ropa ligera, impermeable, protector solar y mantente hidratado durante las lluvias.")

    # 43. Clima cálido (26-35°C), baja humedad (0-30), alto UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def calido_baja_humedad_uv_alto_viento_moderado_despejado(self):
        self.consejos.append("Clima cálido y seco, con UV alto y viento moderado. Usa ropa ligera, gafas de sol, protector solar y una chaqueta ligera para el viento.")

    # 44. Clima cálido (26-35°C), baja humedad (0-30), alto UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad <= 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def calido_baja_humedad_uv_alto_viento_moderado_lluvia(self):
        self.consejos.append("Clima cálido y seco, con UV alto, viento moderado y lluvia. Usa ropa ligera, impermeable y protector solar.")

    # 45. Clima cálido (26-35°C), alta humedad (31-60), alto UV, viento calmado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=1))  # Despejado
    def calido_alta_humedad_uv_alto_viento_calma_despejado(self):
        self.consejos.append("Clima cálido y húmedo con UV alto. Usa ropa ligera, gafas de sol, protector solar y mantente bien hidratado.")

    # 46. Clima cálido (26-35°C), alta humedad (31-60), alto UV, viento calmado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 0)),
          Meteo(sol=2))  # Lluvia
    def calido_alta_humedad_uv_alto_viento_calma_lluvia(self):
        self.consejos.append("Clima cálido y húmedo con UV alto y lluvia. Usa ropa ligera, impermeable y mantente bien hidratado.")

    # 47. Clima cálido (26-35°C), alta humedad (31-60), alto UV, viento moderado, despejado
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=1))  # Despejado
    def calido_alta_humedad_uv_alto_viento_moderado_despejado(self):
        self.consejos.append("Clima cálido y húmedo con UV alto y viento moderado. Usa ropa ligera, protector solar, gafas de sol y mantente hidratado.")

    # 48. Clima cálido (26-35°C), alta humedad (31-60), alto UV, viento moderado, lluvia
    @Rule(Meteo(temp=P(lambda temp: 26 <= temp <= 35)),
          Meteo(humedad=P(lambda humedad: humedad > 30)),
          Meteo(uv=P(lambda uv: uv == 5)),
          Meteo(viento=P(lambda viento: viento == 10)),
          Meteo(sol=2))  # Lluvia
    def calido_alta_humedad_uv_alto_viento_moderado_lluvia(self):
        self.consejos.append("Clima cálido y húmedo con UV alto, viento moderado y lluvia. Usa ropa ligera, impermeable, protector solar y una chaqueta cortavientos.")
        
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
sol_var = tk.IntVar()  # 1: Despejado, 2: Lluvia

# Función llamada cuando el usuario envía sus elecciones
def enviar_opciones():
    temp = temp_var.get()
    humedad = humedad_var.get()
    uv = uv_var.get()
    viento = viento_var.get()
    sol = sol_var.get()
    
    # Ejecutar motor
    consejero = ConsejeroVestimentario()
    consejero.reset()

    consejero.declare(Meteo(temp=temp, humedad=humedad, uv=uv, viento=viento, sol=sol, precip=sol))
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
tk.Radiobutton(root, text="Calmado", variable=viento_var, value=0).pack()
tk.Radiobutton(root, text="Moderado", variable=viento_var, value=10).pack()

# Widgets para la condición del día
tk.Label(root, text="Condición del día:").pack()
tk.Radiobutton(root, text="Despejado", variable=sol_var, value=1).pack()
tk.Radiobutton(root, text="Lluvia", variable=sol_var, value=2).pack()

# Botón de envío
submit_button = tk.Button(root, text="Enviar", command=enviar_opciones)
submit_button.pack()

# Ejecutar la aplicación Tkinter
root.mainloop()
