import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog
from itertools import combinations

def region_factible(coefficients, bounds, signs, max_x = None, max_y = None):
  if not max_x or not max_y:
    # Calculate max_x and max_y (max_x1 and max_x2)
    divisions_x = bounds / coefficients[:, 0]
    max_x = divisions_x[~np.isinf(divisions_x)].max() + 10
    divisions_y = bounds / coefficients[:, 1]
    max_y = divisions_y[~np.isinf(divisions_y)].max() + 10

  x1_vals = np.linspace(-10, max_x, 1000)
  x2_vals = np.linspace(-10, max_y, 1000)
  x1_grid, x2_grid = np.meshgrid(x1_vals, x2_vals)

  feasible = np.ones_like(x1_grid, dtype=bool)

  # Add the constraints for x1 >= 0 and x2 >= 0
  coefficients = np.vstack([coefficients, [[1, 0], [0, 1]]])
  bounds = np.append(bounds, [0, 0])
  signs = signs + ['≥', '≥']

  for coef, bnd, sign in zip(coefficients, bounds, signs):
    if sign == '≤':
        feasible &= coef[0] * x1_grid + coef[1] * x2_grid <= bnd
    elif sign == '≥':
        feasible &= coef[0] * x1_grid + coef[1] * x2_grid >= bnd
    elif sign == '=':
        feasible &= np.isclose(coef[0] * x1_grid + coef[1] * x2_grid, bnd)

  fig, ax = plt.subplots()
  ax.contourf(x1_grid, x2_grid, feasible, levels=[0.5, 1], colors=['lightblue'], alpha=0.5)

  for coef, bnd, sign in zip(coefficients[:-2], bounds[:-2], signs[:-2]):
    if coef[1] != 0:
      y = (bnd - coef[0] * x1_vals) / coef[1]
      ax.plot(x1_vals, y, label=f'{coef[0]}*x1 + {coef[1]}*x2 {sign} {bnd}')
    else:
      ax.axvline(x=bnd/coef[0], color='red', linestyle='--', label=f'x1 {sign} {bnd/coef[0]}')

  ax.axhline(y = 0, color = "black", linestyle = "--", label = "Y = 0")
  ax.axvline(x = 0, color = "black", linestyle = "--", label = "X = 0")

  vertices = []
  # Find vertices by solving pairs of constraints
  for (coef1, bnd1, sign1), (coef2, bnd2, sign2) in combinations(zip(coefficients, bounds, signs), 2):
    A = np.array([coef1, coef2])
    B = np.array([bnd1, bnd2])
    if np.linalg.det(A) != 0:  # Ensure lines are not parallel
      intersection = np.linalg.solve(A, B)
      if all(check_constraint(intersection, coef, bnd, sign) for coef, bnd, sign in zip(coefficients, bounds, signs)):
          if np.all(intersection >= 0):  # Ensure positive coordinates
              vertices.append(intersection)

  for vertex in vertices:
    ax.plot(*vertex, 'ro')

  ax.set_xlim(-1, max_x)
  ax.set_ylim(-1, max_y)
  ax.set_xlabel('x1')
  ax.set_ylabel('x2')
  ax.legend()

  return np.array(vertices), fig

def check_constraint(point, coef, bnd, sign):
    expr_value = np.dot(coef, point)
    if sign == '≤':
        return expr_value <= bnd
    elif sign == '≥':
        return expr_value >= bnd
    elif sign == '=':
        return np.isclose(expr_value, bnd)
    return False

def graphical_method(a1, a2, vertices, mode = "max"):
  max_x = -np.inf
  max_y = -np.inf
  maxi = -np.inf
  min_x = np.inf
  min_y = np.inf
  mini = np.inf
  for vertex in vertices:
    result = a1 * vertex[0] + a2 * vertex[1]
    if result > maxi:
      max_x = vertex[0]
      max_y = vertex[1]
      maxi = result
    if result <  mini:
      min_x = vertex[0]
      min_y = vertex[1]
      mini = result


  return (min_x, min_y, mini), (max_x, max_y, maxi)