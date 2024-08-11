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

def calculate_radius(area):
    return np.sqrt(area / np.pi)

def calculate_area(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def generate_circle_points(cx, cy, radius, num_points=100):
    angles = np.linspace(0, 2 * np.pi, num_points)
    circle_x = cx + radius * np.cos(angles)
    circle_y = cy + radius * np.sin(angles)
    return circle_x, circle_y

def refine_points_to_circle(x, y):
    cx, cy = calculate_centroid(x, y)

    area = calculate_area(x, y)

    radius = calculate_radius(area)

    circle_x, circle_y = generate_circle_points(cx, cy, radius)

    return circle_x, circle_y

def process_circle(input_file, output_file):
    x, y = read_csv(input_file)

    plt.scatter(x, y, label='Original Points')

    x_refined, y_refined = refine_points_to_circle(x, y)

    plt.plot(x_refined, y_refined, color='red', label='Refined Points')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    save_csv(x_refined, y_refined, output_file)