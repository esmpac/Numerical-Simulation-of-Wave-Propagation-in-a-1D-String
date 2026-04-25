# Numerical-Simulation-of-Wave-Propagation-in-a-1D-String

This project implements a numerical simulation of wave propagation on a 1D string using a finite difference method.

## Physical Model

The system is described by the 1D wave equation:

∂²u/∂t² = c² ∂²u/∂x²

with a localized initial perturbation and fixed boundary conditions.

## Numerical Method

The equation is solved using a second-order finite difference scheme:

u_i^{n+1} = 2u_i^n - u_i^{n-1} + λ (u_{i+1}^n - 2u_i^n + u_{i-1}^n)

where λ = (c dt / dx)^2.
