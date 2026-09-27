"""
Regenera las figuras de la Unidad I (Cálculo Actuarial II).

Uso, desde la raíz del repositorio y con el entorno virtual activo:
    python docs/figuras/generar_figuras.py

Las imágenes .png se guardan en la misma carpeta que este script.
Son reconstrucciones de las figuras del PDF original a partir de los
parámetros y datos que aparecen en las notas.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # permite generar imágenes sin abrir ventanas
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle
from scipy import stats

OUT = Path(__file__).resolve().parent


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(OUT / nombre, dpi=150)
    plt.close(fig)


# Figura 1: dos eventos A y B dentro de Omega
def fig1_eventos():
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.add_patch(Rectangle((0, 0), 10, 6, fill=False, lw=1.5))
    ax.add_patch(Circle((4, 3), 2.2, alpha=0.35, color="tab:blue"))
    ax.add_patch(Circle((6, 3), 2.2, alpha=0.35, color="tab:orange"))
    ax.text(2.8, 3, "$A$", fontsize=16, ha="center", va="center")
    ax.text(7.2, 3, "$B$", fontsize=16, ha="center", va="center")
    ax.text(5, 3, r"$A\cap B$", fontsize=11, ha="center", va="center")
    ax.text(9.4, 5.4, r"$\Omega$", fontsize=16)
    ax.set_xlim(-0.2, 10.2)
    ax.set_ylim(-0.2, 6.2)
    ax.set_aspect("equal")
    ax.axis("off")
    guardar(fig, "fig01_eventos.png")


# Figura 2: Bernoulli con p = 0.20
def fig2_bernoulli():
    p = 0.20
    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.bar([0, 1], [1 - p, p], width=0.4)
    ax.set_xticks([0, 1])
    ax.set_ylim(0, 1)
    ax.set_xlabel("$x$")
    ax.set_ylabel(r"$P(X=x)$")
    ax.set_title("Bernoulli con $p = 0.20$")
    guardar(fig, "fig02_bernoulli.png")


# Figura 3: Binomial n = 50, p = 0.04
def fig3_binomial():
    k = np.arange(0, 11)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.bar(k, stats.binom.pmf(k, n=50, p=0.04))
    ax.set_xticks(k)
    ax.set_xlabel("Número de eventos $k$")
    ax.set_ylabel(r"$P(N=k)$")
    ax.set_title("Binomial: $n = 50$, $p = 0.04$")
    guardar(fig, "fig03_binomial.png")


# Figura 4: Poisson con lambda = 2
def fig4_poisson():
    k = np.arange(0, 11)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.bar(k, stats.poisson.pmf(k, mu=2))
    ax.set_xticks(k)
    ax.set_xlabel("Número de reclamaciones $k$")
    ax.set_ylabel(r"$P(N=k)$")
    ax.set_title(r"Poisson con $\lambda = 2$")
    guardar(fig, "fig04_poisson.png")


# Figura 5: densidad exponencial con lambda = 0.20
def fig5_exponencial():
    lam = 0.20
    t = np.linspace(-2, 22, 600)
    f = np.where(t >= 0, lam * np.exp(-lam * np.clip(t, 0, None)), 0.0)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(t, f)
    ax.set_xlabel("$t$")
    ax.set_ylabel("$f_T(t)$")
    ax.set_title(r"Densidad exponencial con $\lambda = 0.20$")
    guardar(fig, "fig05_exponencial.png")


# Figura 6: ley de los grandes números, Bernoulli p = 0.08, semilla 31415
def fig6_lgn():
    rng = np.random.default_rng(31415)
    x = rng.binomial(n=1, p=0.08, size=10_000)
    n = np.arange(1, x.size + 1)
    frecuencia = np.cumsum(x) / n
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.plot(n[9:], frecuencia[9:], label="Frecuencia simulada")
    ax.axhline(0.08, ls="--", color="tab:red", label="$p = 0.08$")
    ax.set_xscale("log")
    ax.set_xlim(10, 10_000)
    ax.set_xlabel("Número acumulado de observaciones")
    ax.set_ylabel("Frecuencia observada")
    ax.set_title("Simulación Bernoulli con $p = 0.08$ y semilla 31415")
    ax.legend()
    guardar(fig, "fig06_ley_grandes_numeros.png")


# Figuras 7 y 8: datos INEGI EDR 2015-2024
ANIOS = list(range(2015, 2025))
DEFUNCIONES = [655688, 685766, 703047, 722611, 747784,
               1086743, 1122249, 847716, 799869, 819672]
TASA = [536, 555, 563, 574, 588, 860, 879, 659, 619, 630]


def fig7_defunciones():
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.plot(ANIOS, DEFUNCIONES, marker="o")
    ax.set_xticks(ANIOS)
    ax.ticklabel_format(axis="y", style="plain")
    ax.set_xlabel("Año")
    ax.set_ylabel("Defunciones registradas")
    ax.set_title("México: defunciones registradas, 2015–2024")
    guardar(fig, "fig07_defunciones_inegi.png")


def fig8_tasa():
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.plot(ANIOS, TASA, marker="o")
    ax.set_xticks(ANIOS)
    ax.set_xlabel("Año")
    ax.set_ylabel("Tasa bruta por 100 mil")
    ax.set_title("México: tasa bruta de defunciones registradas, 2015–2024")
    guardar(fig, "fig08_tasa_bruta_inegi.png")


if __name__ == "__main__":
    for funcion in (fig1_eventos, fig2_bernoulli, fig3_binomial, fig4_poisson,
                    fig5_exponencial, fig6_lgn, fig7_defunciones, fig8_tasa):
        funcion()
    print(f"Figuras guardadas en {OUT}")
