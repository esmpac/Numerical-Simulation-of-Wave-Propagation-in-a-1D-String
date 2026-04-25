# Numerical-Simulation-of-Wave-Propagation-in-a-1D-String

This project implements a numerical simulation of wave propagation on a 1D string using a finite difference method.

## Physical Model

The system is described by the 1D wave equation:

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$$

with a localized initial perturbation and fixed boundary conditions.

## Numerical Method

The equation is solved using a second-order finite difference scheme:

$$
u_i^{n+1} = 2u_i^n - u_i^{n-1} + \lambda (u_{i+1}^n - 2u_i^n + u_{i-1}^n)
$$
where $\lambda = (c \, dt / dx)^2$

## Discussion

The simulation reproduces wave propagation with expected behavior.

The method is simple and efficient, but introduces numerical dispersion and requires stability conditions (CFL).
