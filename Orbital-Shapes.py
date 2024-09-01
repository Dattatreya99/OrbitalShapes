import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm, genlaguerre, factorial
import tkinter as tk
from tkinter import simpledialog
from joblib import Parallel, delayed

def radial_wavefunction(n, l, r, Zeff=1):
    rho = 2 * Zeff * r / n
    L = genlaguerre(n - l - 1, 2 * l + 1)
    prefactor = np.sqrt((2 * Zeff / n)**3 * factorial(n - l - 1) / (2 * n * factorial(n + l)))
    R_nl = prefactor * np.exp(-rho / 2) * (rho**l) * L(rho)
    return R_nl

def main_code(n, l, m):
    a0 = 1  # Bohr radius (arbitrary units)
    Zeff = 1  # Effective nuclear charge (for hydrogen Zeff=1)

    # Adjust grid resolution based on quantum numbers
    r_points = 100 if n < 5 else 150
    theta_points = 40 if l < 3 else 50
    phi_points = 80 if m < 2 else 100

    r = np.linspace(0, 30, r_points)
    theta = np.linspace(0, np.pi, theta_points)
    phi = np.linspace(0, 2 * np.pi, phi_points)

    R, Theta, Phi = np.meshgrid(r, theta, phi, indexing='ij')

    radial = radial_wavefunction(n, l, R)

    Y_lm = sph_harm(m, l, Phi, Theta)
    psi_real = np.real(radial * Y_lm)

    X = R * np.sin(Theta) * np.cos(Phi)
    Y = R * np.sin(Theta) * np.sin(Phi)
    Z = R * np.cos(Theta)

    X, Y, Z, psi_real = [arr.flatten() for arr in (X, Y, Z, psi_real)]

    # Dynamic mask threshold
    threshold = 0.001 * (n / 2)
    mask = np.abs(psi_real) > threshold
    x, y, z, prob = X[mask], Y[mask], Z[mask], psi_real[mask]

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, c=prob, cmap='viridis', s=1)

    ax.set_title(f'Hydrogen-like Orbital: n={n}, l={l}, m={m}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    cbar = fig.colorbar(scatter, shrink=0.5, aspect=5)
    cbar.set_label('Wavefunction (Real Part)')

    plt.tight_layout()
    plt.show()

def get_input_values():
    root = tk.Tk()
    root.withdraw()
    n = simpledialog.askinteger("Input", "Enter the principal quantum number (n):", minvalue=1, maxvalue=10)
    l = simpledialog.askinteger("Input", "Enter the orbital angular momentum quantum number (l):", minvalue=0, maxvalue=n-1)
    m = simpledialog.askinteger("Input", "Enter the magnetic quantum number (m):", minvalue=-l, maxvalue=l)
    return n, l, m

if __name__ == "__main__":
    n, l, m = get_input_values()
    main_code(n, l, m)
