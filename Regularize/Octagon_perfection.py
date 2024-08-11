import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from read_csv import read_csv
from save_csv import save_csv

def calculate_centroid(x, y):
    return np.mean(x), np.mean(y)

def calculate_area(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def generate_octagon_points(cx, cy, radius):
    angles = np.linspace(0, 2 * np.pi, 9)[:-1]  # 8 vertices + closing point
    octagon_x = cx + radius * np.cos(angles)
    octagon_y = cy + radius * np.sin(angles)
    return octagon_x, octagon_y

def calculate_octagon_radius(area):
    return np.sqrt(area / (2 * (1 + np.sqrt(2))))

def process_octagon(input_file, output_file):
    x, y = read_csv(input_file)

    plt.scatter(x, y, label='Original Points')

    cx, cy = calculate_centroid(x, y)

    area = calculate_area(x, y)

    radius = calculate_octagon_radius(area)

    x_refined, y_refined = generate_octagon_points(cx, cy, radius)

    plt.plot(np.append(x_refined, x_refined[0]), np.append(y_refined, y_refined[0]), color='red', label='Refined Points')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    save_csv(x_refined, y_refined, output_file)