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

def calculate_side_length(area):
    return np.sqrt(area)

def generate_square_points(cx, cy, side_length):
    half_side = side_length / 2
    square_x = [cx - half_side, cx + half_side, cx + half_side, cx - half_side]
    square_y = [cy - half_side, cy - half_side, cy + half_side, cy + half_side]
    return np.array(square_x), np.array(square_y)

def calculate_area(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def refine_points_to_square(x, y):
    cx, cy = calculate_centroid(x, y)

    area = calculate_area(x, y)

    side_length = calculate_side_length(area)

    # Generate perfect square points
    square_x, square_y = generate_square_points(cx, cy, side_length)

    return square_x, square_y

def process_square(input_file, output_file):
    x, y = read_csv(input_file)

    plt.scatter(x, y, label='Original Points')

    x_refined, y_refined = refine_points_to_square(x, y)

    plt.plot(np.append(x_refined, x_refined[0]), np.append(y_refined, y_refined[0]), color='red', label='Refined Points')
    plt.legend()
    plt.show()

    save_csv(np.append(x_refined, x_refined[0]), np.append(y_refined, y_refined[0]), output_file)