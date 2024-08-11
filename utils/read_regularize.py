import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv_adobe ( csv_path ):
    np_path_XYs = np . genfromtxt ( csv_path , delimiter = ',')
    path_XYs = []
    for i in np . unique ( np_path_XYs [: , 0]):
        npXYs = np_path_XYs [ np_path_XYs [: , 0] == i ][: , 1:]
        XYs = []
        for j in np . unique ( npXYs [: , 0]):
            XY = npXYs [ npXYs [: , 0] == j ][: , 1:]
            XYs . append ( XY )
            path_XYs . append ( XYs )
    return path_XYs

    
def plot_csv(paths_XYs):
    fig, ax = plt.subplots(tight_layout=True, figsize=(6, 6))
    for i, XYs in enumerate(paths_XYs):
        for XY in XYs:
            ax.plot(XY[:, 0], XY[:, 1], linewidth=2)
    
    ax.set_aspect('equal')
    ax.axis('off') 
    plt.show()
    
def plot_and_save(paths_XYs, save_path=None):
    fig, ax = plt.subplots(tight_layout=True, figsize=(6, 6))
    for i, XYs in enumerate(paths_XYs):
        for XY in XYs:
            ax.plot(XY[:, 0], XY[:, 1], linewidth=2)
    
    ax.set_aspect('equal')
    ax.axis('off')
    if(save_path):
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0, facecolor='white')
    plt.show()


def plot_csv_by_id(csv_file):
    df = pd.read_csv(csv_file, header=None, names=['ID', 'Zero', 'X', 'Y'])
    
    unique_ids = df['ID'].unique()
    
    plt.figure(figsize=(4, 4))
    for shape_id in unique_ids:
        subset = df[df['ID'] == shape_id]
        plt.scatter(subset['X'], subset['Y'], label=f'ID {shape_id}', s=1)
    
    plt.axis('off')
    plt.gca().invert_yaxis()  
    plt.show()