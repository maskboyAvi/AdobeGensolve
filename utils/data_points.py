import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import label

def process_image(image_path, threshold=200):
    # Load the image and convert to grayscale
    image = Image.open(image_path).convert('L')
    
    # Convert image to black and white
    bw_image = image.point(lambda p: p > threshold and 255)
    bw_array = np.array(bw_image)
    
    # Find connected components
    labeled_array, num_features = label(bw_array == 0)  # Find connected components where pixel is black (0)
    
    # Extract coordinates of points in each connected component
    connected_components = {}
    for component_id in range(1, num_features + 1):
        coords = np.column_stack(np.where(labeled_array == component_id))
        connected_components[component_id] = coords
    
    return connected_components

def plot_connected_components(connected_components, image_shape):
    # Plot the connected components
    fig, ax = plt.subplots(figsize=(6, 6))
    colors = plt.cm.get_cmap('hsv', len(connected_components) + 1)
    
    for component_id, coords in connected_components.items():
        ax.plot(coords[:, 1], image_shape[0] - coords[:, 0], 'o', markersize=1, color=colors(component_id))
    
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()
