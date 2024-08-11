import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_centroid(x, y):
    return np.mean(x), np.mean(y)

# Function to generate points for a perfect star centered at (cx, cy)
def generate_star_points(cx, cy, radius, num_points=5):
    angles = np.linspace(0, 2 * np.pi, 2 * num_points + 1)
    points_x = []
    points_y = []
    for i, angle in enumerate(angles):
        if i % 2 == 0:
            points_x.append(cx + radius * np.cos(angle))
            points_y.append(cy + radius * np.sin(angle))
        else:
            points_x.append(cx + (radius / 2) * np.cos(angle))
            points_y.append(cy + (radius / 2) * np.sin(angle))
    return np.array(points_x), np.array(points_y)

# Main function to process the CSV file
def process_star(input_file, output_file):
    x, y = read_csv(input_file)

    # Plot the original points
    plt.scatter(x, y, label='Original Points')

    # Calculate the centroid of the original points
    cx, cy = calculate_centroid(x, y)

    # Assume a radius that maintains the original scale (e.g., the maximum distance from the centroid)
    radius = np.max(np.sqrt((x - cx)**2 + (y - cy)**2))

    # Generate star points
    x_refined, y_refined = generate_star_points(cx, cy, radius, num_points=5)

    # Plot the refined points
    plt.plot(np.append(x_refined, x_refined[0]), np.append(y_refined, y_refined[0]), color='red', label='Refined Points')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    save_csv(x_refined, y_refined, output_file)