import math
import tkinter as tk
from tkinter import messagebox, ttk

# ---------------------------
#   CONSTANTES
# ---------------------------
ts = 0.3
Tm = 450
Tr = 20
Ta = 27
Ko = 242
ar = 0.00381
pr = 1.78
Tcap = 3.42
Rc = 1000
hs = 0.10
ps = 3000
Cs = 0.691
d = 0.01168
n = 6
h = 0.5
Kii = 1
ho = 1
Df = 1.043
Sf = 0.60
Lr = 2.4

# ---------------------------
#  FUNCIÓN DE CÁLCULO
# ---------------------------
def calcular():
    try:
        ValorIo = float(Io.get())
        Valorp = float(p.get())
        ValorLx = float(Lx.get())
        ValorLy = float(Ly.get())
        ValorDt = float(Dt.get())
        ValorNr = float(Nr.get())

        # ---------------------------
        #   CÁLCULOS
        # ---------------------------

        Acalculada = (ValorIo) / (((Tcap * 0.0001) / ((ar * pr) * ts)) * (math.log((Ko + Tm) / (Ko + Ta))))**0.5
        Acalculada1 = Acalculada * 0.001

        k = (Valorp - ps) / (Valorp + ps)

        Et50 = ((Rc + (1.5 * (Cs * ps))) * (0.116)) / (ts)**0.5
        Ep50 = ((Rc + (6 * (Cs * ps))) * (0.116)) / (ts)**0.5

        Ki = 0.65 + (0.148 * n)
        Kh = (1 + (h / ho))**0.5

        Km = ((1 / (2 * math.pi)) *
             (math.log(((ValorDt**2) / (16*h*d)) +
                       (((ValorDt + 2*h)**2) / (8*ValorDt*d)) -
                       (h / (4*d)))
              + ((Kii / Kh) * (math.log(8 / (((2*n)-1)*math.pi))))))

        Lcal = ((Km * Ki) * (Valorp * ValorIo) * (ts**0.5)) / (116 + (0.174 * (Cs * ps)))

        Am = ValorLx * ValorLy

        N = int(ValorLx / ValorDt) + 1
        M = int(ValorLy / ValorDt) + 1

        Lrt = ValorNr * Lr
        Lc = (N * ValorLx) + (M * ValorLy)
        Lt = Lc + Lrt

        Rg = Valorp * ((1 / Lt) + ((1 / (20 * Am)**0.5) * (1 + (1 / (1 + (h * (20 / Am)**0.5))))))

        Ig = Df * ValorIo * Sf
        Gpr = Ig * Rg

        Em = (Valorp * Ig * Km * Ki) / (Lt + ((1.55 + (1.22 * (Lr / ((ValorLx**2)+(ValorLy**2))**0.5))) * Lrt))
        Ks = (1 / math.pi) * ((1 / (2*h)) + (1 / (ValorDt + h)) + ((1 - 0.5**(n - 2)) / ValorDt))
        Es = (Valorp * Ig * Ks * Ki) / (0.75 * Lc + 0.85 * Lrt)

        if Rg > 1:
            raise ValueError("Disminuya el valor del ancho de la cuadricula (D).")

        if Em > Et50:
            raise ValueError("La tensión de retícula es mayor que la tensión de toque permitida.")

        if Es > Ep50:
            raise ValueError("La tensión de paso es mayor que la permitida.")

        # ---------------------------
        #   MOSTRAR RESULTADOS
        # ---------------------------
        resultado_texto = f"""
------------- RESULTADOS -------------
CORRIENTE DE FALLA A TIERRA, Io:
    {ValorIo:.3f}

RESISTIVIDAD DEL TERRENO (Ω·m), p:
    {Valorp:.3f}

ÁREA DE LA MALLA, A:
    {Am:.3f}

CONDUCTOR UTILIZADO:
    4/0 AWG

PROFUNDIDAD DE ENTERRAMIENTO (h):
    {h} m

RESISTENCIA DE PUESTA A TIERRA, Rg:
    {Rg:.4f} Ω

MÁX. TENSIÓN DE LA MALLA (GPR):
    {Gpr:.3f} V

TENSIÓN DE TOQUE TOLERABLE (50 kg), Et-50:
    {Et50:.3f} V

TENSIÓN DE PASO TOLERABLE (50 kg), Ep-50:
    {Ep50:.3f} V

TENSIÓN DE RETÍCULA, Em:
    {Em:.3f} V

TENSIÓN DE PASO, Es:
    {Es:.3f} V
"""


        cuadro_resultados.config(state="normal")
        cuadro_resultados.delete(1.0, tk.END)
        cuadro_resultados.insert(tk.END, resultado_texto)
        cuadro_resultados.config(state="disabled")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


# ---------------------------
#    INTERFAZ TKINTER
# ---------------------------
ventana = tk.Tk()
ventana.title("Cálculos de Malla a Tierra")

tk.Label(ventana, text="Corriente eficaz (I):").grid(row=0, column=0)
Io = tk.Entry(ventana)
Io.grid(row=0, column=1)

tk.Label(ventana, text="Resistividad del terreno (p):").grid(row=1, column=0)
p = tk.Entry(ventana)
p.grid(row=1, column=1)

tk.Label(ventana, text="Ancho de la malla (Lx):").grid(row=2, column=0)
Lx = tk.Entry(ventana)
Lx.grid(row=2, column=1)

tk.Label(ventana, text="Largo de la malla (Ly):").grid(row=3, column=0)
Ly = tk.Entry(ventana)
Ly.grid(row=3, column=1)

tk.Label(ventana, text="Ancho de cuadrícula (D):").grid(row=4, column=0)
Dt = tk.Entry(ventana)
Dt.grid(row=4, column=1)

tk.Label(ventana, text="Número de electrodos (Nr):").grid(row=5, column=0)
Nr = tk.Entry(ventana)
Nr.grid(row=5, column=1)

tk.Button(ventana, text="Calcular", command=calcular).grid(row=6, column=0, columnspan=2, pady=10)

# Cuadro donde se mostrarán los resultados
cuadro_resultados = tk.Text(ventana, width=45, height=35, state="disabled", bg="#f0f0f0")
cuadro_resultados.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

ventana.mainloop()
