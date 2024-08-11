import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Function to calculate the centroid of points
def calculate_centroid(x, y):
    return np.mean(x), np.mean(y)

# Function to calculate the radius of the circle based on area
def calculate_radius(area):
    return np.sqrt(area / np.pi)

# Function to calculate the area of a polygon given its vertices
def calculate_area(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

# Function to generate points for a perfect circle centered at (cx, cy)
def generate_circle_points(cx, cy, radius, num_points=100):
    angles = np.linspace(0, 2 * np.pi, num_points)
    circle_x = cx + radius * np.cos(angles)
    circle_y = cy + radius * np.sin(angles)
    return circle_x, circle_y

# Function to refine points to match a perfect circle
def refine_points_to_circle(x, y):
    # Calculate the centroid of the original points
    cx, cy = calculate_centroid(x, y)

    # Calculate the area of the original shape
    area = calculate_area(x, y)

    # Calculate the radius of the circle
    radius = calculate_radius(area)

    # Generate perfect circle points
    circle_x, circle_y = generate_circle_points(cx, cy, radius)

    return circle_x, circle_y

# Main function to process the CSV file
def process_circle(input_file, output_file):
    x, y = read_csv(input_file)

    # Plot the original points
    plt.scatter(x, y, label='Original Points')

    x_refined, y_refined = refine_points_to_circle(x, y)

    # Plot the refined points
    plt.plot(x_refined, y_refined, color='red', label='Refined Points')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    save_csv(x_refined, y_refined, output_file)