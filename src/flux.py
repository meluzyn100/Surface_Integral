import numpy as np
import sympy as sp
from sympy.abc import x, y, z
from sympy.utilities.lambdify import lambdify
from typing import List, Union

# Define symbolic variables for parameters
u = sp.symbols("u")
v = sp.symbols("v")


def derivative_u(f: List[sp.Expr], h: float = 0.001) -> List[sp.Expr]:
    """
    Compute the partial derivative with respect to 'u' of the given parametric function f.

    Parameters:
        f (List[sp.Expr]): List of symbolic expressions representing the parametric function.
        h (float): Step size for numerical differentiation (default: 0.001).

    Returns:
        List[sp.Expr]: Partial derivative with respect to 'u'.
    """
    return [(f[i].subs(u, u + h) - f[i]) / h if i < len(f) else 0 for i in range(3)]


def derivative_v(f: List[sp.Expr], h: float = 0.001) -> List[sp.Expr]:
    """
    Compute the partial derivative with respect to 'v' of the given parametric function f.

    Parameters:
        f (List[sp.Expr]): List of symbolic expressions representing the parametric function.
        h (float): Step size for numerical differentiation (default: 0.001).

    Returns:
        List[sp.Expr]: Partial derivative with respect to 'v'.
    """
    return [(f[i].subs(v, v + h) - f[i]) / h if i < len(f) else 0 for i in range(3)]


def flux(
    F: List[sp.Expr],
    r: List[sp.Expr],
    u_lim: List[Union[float, sp.Expr]],
    v_lim: List[Union[float, sp.Expr]],
    dx: float = 0.001,
) -> float:
    """
    Numerically compute the flux through a parametric surface.

    Parameters:
        F (List[sp.Expr]): Vector function F(x, y, z).
        r (List[sp.Expr]): Parametric surface r(u, v).
        u_lim (List[Union[float, sp.Expr]]): Bounds of the parameter 'u' as [u_min, u_max].
        v_lim (List[Union[float, sp.Expr]]): Bounds of the parameter 'v' as [v_min, v_max].
        dx (float): Step size for the numerical double integral (default: 0.001).

    Returns:
        float: Computed flux through the surface.
    """
    # Compute partial derivatives of the parametric surface
    r_u = derivative_u(r, h=dx)
    r_v = derivative_v(r, h=dx)

    F_param = []
    for i in range(3):
        try:
            F_param.append(F[i].subs([(x, r[0]), (y, r[1]), (z, r[2])]))
        except:
            F_param.append(0)

    normal_vector = np.cross(r_u, r_v)

    # Compute the dot product of F and the normal vector
    dot_product = np.dot(F_param, normal_vector) * dx**2

    # Optimize the computation using lambdify
    flux_function = lambdify([u, v], dot_product, modules="numpy")

    # Compute the flux values for each point on the surface
    flux_values = [
        flux_function(u + dx / 2, v + dx / 2)
        for u in np.arange(u_lim[0], u_lim[1], dx)
        for v in np.arange(eval(str(v_lim[0])), eval(str(v_lim[1])), dx)
    ]

    # Return the total flux, ignoring NaN values
    return np.nansum(flux_values)
