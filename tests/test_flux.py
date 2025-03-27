from flux import flux  # Import after modifying sys.path
import sys
import unittest
import math
import random
import sympy as sp
from sympy.abc import x, y, z
from pathlib import Path

# Set a default seed for randomization
random.seed(777)
# Add the src directory to the Python module search path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))


# Define symbolic variables for parameters
u = sp.symbols("u")
v = sp.symbols("v")
pi = math.pi


class TestFlux(unittest.TestCase):
    """
    Unit tests for the flux function.
    """

    def calculate_errors(
        self, computed: float, expected: float, tolerance: float = 0.01
    ) -> None:
        """
        Helper method to assert that the computed value is within a given tolerance of the expected value.

        Parameters:
            computed (float): The computed flux value.
            expected (float): The expected flux value.
            tolerance (float): The acceptable error margin (default: 1e-3).

        Raises:
            AssertionError: If the computed value is not within the tolerance of the expected value.
        """
        relative_error = abs(computed - expected) / abs(expected)
        self.assertAlmostEqual(
            relative_error,
            0,
            delta=tolerance,
            msg=f"Computed: {computed}, Expected: {expected}, Relative Error: {relative_error}",
        )

    def test_zad3_a(self):
        result = flux([2 * x, 5 * y, 0], [u, v, 4 * u + 3 * v], [0, 1], [-8, 8], 0.005)
        self.calculate_errors(result, -64)

    def test_zad3_b(self):
        result = flux([x**2, y**2, z**2], [u, v, 4 - u - v], [0, 4], [0, 4 - u], 0.0025)
        self.calculate_errors(result, 64)

    def test_zad3_c(self):
        result = flux(
            [x - z, y - x, z - y],
            [u * sp.cos(v), u * sp.sin(v), u],
            [0, 3],
            [0, pi],
            0.005,
        )
        self.calculate_errors(result, -18)

    def test_zad3_d(self):
        result = flux(
            [x, y, z],
            [u * sp.cos(v), u * sp.sin(v), u**2],
            [0, 4],
            [-pi, pi],
            0.0125,
        )
        self.calculate_errors(result, -128 * pi)

    def test_zad3_e(self):
        result = flux(
            [sp.tan(x * y), x**2 * y, -z],
            [u, sp.cos(v), -3 * sp.sin(v)],
            [1, 4],
            [0, 2 * pi],
            0.005,
        )
        self.calculate_errors(result, 54 * pi)

    def test_zad3_f(self):
        result = flux(
            [sp.cosh(y), 0, sp.sinh(x)],
            [u, v, u + v**2],
            [0, 1],
            [0, u],
            0.0025,
        )
        self.calculate_errors(result, 1 - math.sinh(1))

    def test_zad3_g(self):
        result = flux(
            [y**2, x**2, z**4],
            [u, v, 4 * sp.sqrt(u**2 + v**2)],
            [-2, 2],
            [0, (4 - u**2) ** (1 / 2)],
            0.005,
        )
        self.calculate_errors(result, (8192 / 3) * pi)

    def test_zad3_g_ii(self):
        result = flux(
            [y**2, x**2, z**4],
            [u * sp.cos(v), u * sp.sin(v), 4 * u],
            [0, 2],
            [0, pi],
            0.005,
        )
        self.calculate_errors(result, (8192 / 3) * pi)


if __name__ == "__main__":
    unittest.main()
