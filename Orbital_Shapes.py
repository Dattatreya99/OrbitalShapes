import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm, genlaguerre, factorial
import tkinter as tk
from tkinter import simpledialog

# Function to calculate radial wavefunction for hydrogen-like atom
def radial_wavefunction(n, l, r, Zeff=1):
    rho = 2 * Zeff * r / n
    L = genlaguerre(n - l - 1, 2 * l + 1)
    prefactor = np.sqrt((2 * Zeff / n)**3 * factorial(n - l - 1) / (2 * n * factorial(n + l)))
    R_nl = prefactor * np.exp(-rho / 2) * (rho**l) * L(rho)
    return R_nl

# Function to execute the main code
def main_code(n, l, m):
    a0 = 1  # Bohr radius (arbitrary units)
    Zeff = 1  # Effective nuclear charge (for hydrogen Zeff=1)

    # Create a meshgrid for r, theta, phi
    r = np.linspace(0, 30, 150)         
    theta = np.linspace(0, np.pi, 50)   
    phi = np.linspace(0, 2 * np.pi, 100)

    R, Theta, Phi = np.meshgrid(r, theta, phi, indexing='ij')

    # Calculate radial wavefunction
    radial = radial_wavefunction(n, l, R)

    # Spherical harmonics
    Y_lm = sph_harm(m, l, Phi, Theta)

    # Real part of the wavefunction
    psi_real = np.real(radial * Y_lm)

    # Convert spherical to Cartesian coordinates
    X = R * np.sin(Theta) * np.cos(Phi)
    Y = R * np.sin(Theta) * np.sin(Phi)
    Z = R * np.cos(Theta)

    # Flatten arrays
    X = X.flatten()
    Y = Y.flatten()
    Z = Z.flatten()
    psi_real = psi_real.flatten()

    # Plotting
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Mask based on the absolute value of psi_real
    mask = np.abs(psi_real) > 0.001
    x = X[mask]
    y = Y[mask]
    z = Z[mask]
    prob = psi_real[mask]

    # Scatter plot of dots
    scatter = ax.scatter(x, y, z, c=prob, cmap='viridis', s=1)

    # Set plot title and labels
    ax.set_title(f'Hydrogen-like Orbital: n={n}, l={l}, m={m}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Color bar
    cbar = fig.colorbar(scatter, shrink=0.5, aspect=5)
    cbar.set_label('Wavefunction (Real Part)')

    plt.tight_layout()
    plt.show()

# GUI to input n, l, m values
def get_input_values():
    root = tk.Tk()
    root.withdraw()

    n = simpledialog.askinteger("Input", "Enter the principal quantum number (n):", minvalue=1, maxvalue=10)
    l = simpledialog.askinteger("Input", "Enter the orbital angular momentum quantum number (l):", minvalue=0, maxvalue=n-1)
    m = simpledialog.askinteger("Input", "Enter the magnetic quantum number (m):", minvalue=-l, maxvalue=l)

    return n, l, m

# Main function to run the program
if __name__ == "__main__":
    n, l, m = get_input_values()
    main_code(n, l, m)
