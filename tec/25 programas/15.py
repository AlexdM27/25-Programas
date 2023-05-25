import random

def estimate_pi(num_points):
    points_inside_circle = 0
    points_total = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

        points_total += 1

    pi_estimate = 4 * points_inside_circle / points_total
    return pi_estimate

# Estimar pi utilizando 100,000 puntos aleatorios
num_points = 100000
pi_approximation = estimate_pi(num_points)

print("Aproximación de pi:", pi_approximation)
