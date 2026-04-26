# Numerical Simulation of Wave Propagation in a 1D String

This project implements a numerical simulation of wave propagation on a 1D string using a finite difference method (FDM).

---

## Physical Model

The system is described by the 1D wave equation:

$$
\frac{\partial^2 u(x,t)}{\partial t^2} = c^2 \frac{\partial^2 u(x,t)}{\partial x^2}
$$

where:

- $u(x,t)$ is the displacement of the string  
- $c$ is the wave propagation speed  

### Initial condition

A localized initial perturbation:

$$
u(x,0) = f(x)
$$

### Boundary conditions (Dirichlet)

$$
u(0,t) = 0, \quad u(L,t) = 0
$$

---

## Numerical Method

The equation is solved using a second-order finite difference scheme:

$$
u_i^{n+1} = 2u_i^n - u_i^{n-1} + \lambda \left( u_{i+1}^n - 2u_i^n + u_{i-1}^n \right)
$$

where:

$$
\lambda = \left(\frac{c \Delta t}{\Delta x}\right)^2
$$


represents the square of the 'Courant number' ($C$)

$$
\lambda = C^2
$$

---


## Discussion

### Methodological Description (Choice of Discretization Method)
  
To translate the continuous d'Alembert equation into a computational model, the Finite Difference Method (FDM) was adopted.

This numerical technique was selected as the primary discretization strategy due to its efficiency and straightforward application to one-dimensional (1D) domains with regular geometry, such as a vibrating string.

While the Finite Element Method (FEM) excels in handling complex geometries and multidimensional domains, FDM allows for the approximation of differential operators via Taylor series expansions with significantly lower computational overhead, while ensuring high accuracy for the problem under consideration.



### CFL Condition

The simulation reproduces the expected wave propagation behavior.

The method is simple and efficient, but introduces numerical dispersion and requires stability conditions (CFL condition) to ensure accuracy.

The stability condition for the finite difference scheme is:

$$
\frac{c \Delta t}{\Delta x} \le 1
$$

In this simulation:

$$
\frac{c \Delta t}{\Delta x} = 0.2
$$

which satisfies the CFL condition, ensuring numerical stability.


---

## Parameters

The parameters are chosen to satisfy the CFL stability condition and ensure numerical accuracy:

- Wave speed: `c = 1`
- Time step: `dt = 0.2`
- Spatial step: `dx = 1`
- Initial condition: localized pulse

---


## Features

- Finite difference discretization of the wave equation
- Time evolution of an initial localized disturbance
- Visualization of:
  - Full system evolution
  - Zoomed region of the wave packet
- Comparison between current and previous time step

---

## Output

The simulation produces plots showing:

- Wave propagation over time
- Evolution of the initial pulse
- Local zoom of the active region

---

## Requirements

- Python ≥ 3.8
- NumPy
- Matplotlib

Install dependencies with:

```bash
pip install numpy matplotlib
```
---

## Repository Structure

code/      → main Python pipeline  
results/   → plots and figures  


## Author

Developed and maintained by Erasmo Pacini

