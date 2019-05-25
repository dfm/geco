"""
Equation: Vlasov-Poisson
Ansatz:   VP-E-Polytropic-L-Polytropic

This creates a torus solution.
"""

from geco import *

# Create solver
solver = VlasovPoissonSolver()
solver.parameters.output.plot_solution = False

# Create ansatz for initial guess
model = MaterialModel("VP-E-Polytropic-L-Polytropic")
model.parameters.E0 = 1.0
model.parameters.k = 0.0
model.parameters.l = 0.0

# Solve
U, RHO, data = solver.solve(model)

# Plot density
plot(RHO)
interactive()
