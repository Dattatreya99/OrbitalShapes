# Hydrogen-like Atom Wavefunction Visualization

This Python project visualizes the real part of the wavefunction for hydrogen-like atoms. The wavefunction is calculated using spherical coordinates and quantum numbers `n`, `l`, and `m`. The visualization is a 3D scatter plot representing the electron's probability density in space.

## Features

- **3D Visualization**: Generates a 3D scatter plot of the wavefunction's real part.
- **Customizable Input**: Users can input quantum numbers `n`, `l`, and `m` through a simple GUI.

## Prerequisites

Make sure you have Python installed along with the following libraries:

- `numpy`
- `matplotlib`
- `scipy`
- `tkinter`
- `joblib`

### Installation

You can install the required packages using `pip`:

```bash
pip install numpy matplotlib scipy joblib
```
## How to Run the Project.
Clone the Repository:

```bash
git clone https://github.com/Dattatreya99/OrbitalShapes.git
```
## Navigate to the Project Directory:

```bash
cd OrbitalShapes
```

## Run the Python Script:
```bash
python Orbital-Shapes.py
```

## Enter Quantum Numbers:

A GUI will pop up, prompting you to enter the quantum numbers:

n: Principal quantum number (1 ≤ n ≤ 10).
l: Orbital angular momentum quantum number (0 ≤ l ≤ n-1).
m: Magnetic quantum number (-l ≤ m ≤ l).
After entering these values, a 3D visualization of the Orbital for the specific wavefunction will be displayed.

### Understanding the Code.
Radial Wavefunction: The radial part of the wavefunction is calculated using Laguerre polynomials.
Spherical Harmonics: The angular part is computed using spherical harmonics (scipy.special.sph_harm).
Meshgrid: A 3D grid is created for r, theta, and phi coordinates.
Dynamic Mask: A threshold is applied to filter out low-probability regions for better visualization.
3D Plot: The final visualization is a scatter plot with color representing the real part of the wavefunction.

### License.
This project is licensed under the Apache License 2.0.
You are free to use, modify, and distribute this code, but you must give credit to the original author. 
Patent rights are retained by the author.

## Contributions
Contributions are welcome! 
Please fork the repository and submit a pull request if you have any improvements or bug fixes.

## Author
This code was developed by Dattatreya Mangipudi. If you have any questions or suggestions, feel free to contact me:.

Email: mssdatta2@gmail.com.  
Mobile: 8179459209.  
LinkedIn: https://www.linkedin.com/in/dattatreya-mangipudi-7168762a6/.  
