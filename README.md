# Numerical Simulation of Wave Propagation in a 1D String

This project implements a numerical simulation of wave propagation on a 1D string using a finite difference method.

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
\lambda = \left( \frac{c \Delta t}{\Delta x} \right)^2
$$
---

## ⚙️ Parameters

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

## Discussion

The simulation reproduces the expected wave propagation behavior.

The method is simple and efficient, but introduces numerical dispersion and requires stability conditions (CFL condition) to ensure accuracy.

---

## Requirements

- Python ≥ 3.8
- NumPy
- Matplotlib

Install dependencies with:

```bash
pip install numpy matplotlib
```
