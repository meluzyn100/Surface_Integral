# Surface_Integral

This repository provides a Python implementation for numerically computing the flux of a vector field through a parametric surface using double integrals. The implementation is based on symbolic computation with `sympy` and numerical integration with `numpy`.

## Features

- Compute the flux of a vector field through a parametric surface.
- Symbolic differentiation for partial derivatives of parametric surfaces.
- Numerical integration using a grid-based approach.
- Unit tests to validate the implementation against known results.
- Jupyter Notebook for interactive exploration and visualization.

## Repository Structure

.gitignore
Flux_notebook.ipynb       # Jupyter Notebook for interactive exploration
LICENSE                   # MIT License
README.md                 # Project documentation
requirements.txt          # Python dependencies
figure/
    koło-kwadrat.png      # Supporting image for the notebook
src/
    flux.py               # Core implementation of the flux computation
tests/
    test_flux.py          # Unit tests for the flux computation

### Key Files

1. **src/flux.py**:
   - Contains the implementation of the `flux` function, which computes the flux through a parametric surface.
   - Includes helper functions for symbolic differentiation (`derivative_u` and `derivative_v`).

2. **tests/test_flux.py**:
   - Unit tests for the `flux` function using `unittest`.
   - Validates the implementation against a variety of test cases with known results.

3. **Flux_notebook.ipynb**:
   - Jupyter Notebook demonstrating the numerical computation of flux through various surfaces.
   - Includes detailed explanations, equations, and examples.

4. **requirements.txt**:
   - Lists the Python dependencies required to run the project:
     - `numpy`
     - `sympy`

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/Surface_Integral.git
   cd Surface_Integral

2. Install the required dependencies:
   pip install -r requirements.txt

## Usage

### Running the Flux Computation

You can use the `flux` function from the `src/flux.py` file to compute the flux of a vector field through a parametric surface. Example usage:
```python
from src.flux import flux
from sympy.abc import x, y, z
import sympy as sp

u, v = sp.symbols("u v")
result = flux(
    F=[2 * x, 5 * y, 0],
    r=[u, v, 4 * u + 3 * v],
    u_lim=[0, 1],
    v_lim=[-8, 8],
    dx=0.005
)
print("Computed Flux:", result)
```

### Running Tests

To run the unit tests, execute the following command:

python -m unittest discover tests

### Exploring the Notebook

Open the Jupyter Notebook for an interactive exploration:

jupyter notebook Flux_notebook.ipynb

## Examples

The repository includes several test cases and examples, such as:

1. Computing flux through a plane, sphere, or paraboloid.
2. Validating results against known analytical solutions.
3. Analyzing numerical errors based on grid resolution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flux Integrals - Oregon State University](http://sites.science.oregonstate.edu/math/home/programs/undergrad/CalculusQuestStudyGuides/vcalc/flux/flux.html)
- [Double Integrals - Paul's Online Math Notes](https://tutorial.math.lamar.edu/classes/calciii/DoubleIntegrals.aspx)