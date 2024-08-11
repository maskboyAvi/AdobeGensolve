import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import read_csv,save_csv
def calculate_centroid(x, y):
    return np.mean(x), np.mean(y)

def calculate_area(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def generate_hexagon_points(cx, cy, radius):
    angles = np.linspace(0, 2 * np.pi, 7)[:-1]  # 6 vertices + closing point
    hexagon_x = cx + radius * np.cos(angles)
    hexagon_y = cy + radius * np.sin(angles)
    return hexagon_x, hexagon_y

def calculate_hexagon_radius(area):
    return np.sqrt((2 * area) / (3 * np.sqrt(3)))

def process_hexagon(input_file, output_file):
    x, y = read_csv(input_file)

    plt.scatter(x, y, label='Original Points')

    cx, cy = calculate_centroid(x, y)

    area = calculate_area(x, y)

    radius = calculate_hexagon_radius(area)

    x_refined, y_refined = generate_hexagon_points(cx, cy, radius)

    plt.plot(np.append(x_refined, x_refined[0]), np.append(y_refined, y_refined[0]), color='red', label='Refined Points')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    save_csv(x_refined, y_refined, output_file)