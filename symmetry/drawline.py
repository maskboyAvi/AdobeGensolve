import cv2
import numpy as np
import os

def find_symmetry_lines(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Threshold the image to get a binary image
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) == 0:
        print("No contours found!")
        return []
    
    # Assume the largest contour is the shape we want to analyze
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Calculate the moments of the contour
    M = cv2.moments(largest_contour)
    
    if M['m00'] == 0:
        print("Contour has no area!")
        return []
    
    # Calculate the centroid of the shape
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    
    # Determine the shape type based on the number of vertices
    epsilon = 0.02 * cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, epsilon, True)
    num_vertices = len(approx)

    symmetry_lines = []

    if num_vertices == 4:  # Square or rectangle
        # Vertical and horizontal lines of symmetry
        symmetry_lines.append(((cx, 0), (cx, image.shape[0])))  # Vertical line
        symmetry_lines.append(((0, cy), (image.shape[1], cy)))  # Horizontal line

    elif num_vertices == 5:  # Star shape (pentagon)
        # For a star shape, we can assume symmetry through each vertex
        for i in range(num_vertices):
            angle = (i * 360 / num_vertices) + 90  # Adjust for proper orientation
            angle_rad = np.deg2rad(angle)
            point1 = (int(cx + (image.shape[1] / 2) * np.cos(angle_rad)), int(cy + (image.shape[0] / 2) * np.sin(angle_rad)))
            point2 = (int(cx - (image.shape[1] / 2) * np.cos(angle_rad)), int(cy - (image.shape[0] / 2) * np.sin(angle_rad)))
            symmetry_lines.append((point1, point2))

    elif num_vertices >= 8:  # Circle or other regular shapes
        # Draw lines for every 360/n symmetry
        for i in range(num_vertices):
            angle = (i * 360 / num_vertices) + 90  # Adjust for proper orientation
            angle_rad = np.deg2rad(angle)
            point1 = (int(cx + (image.shape[1] / 2) * np.cos(angle_rad)), int(cy + (image.shape[0] / 2) * np.sin(angle_rad)))
            point2 = (int(cx - (image.shape[1] / 2) * np.cos(angle_rad)), int(cy - (image.shape[0] / 2) * np.sin(angle_rad)))
            symmetry_lines.append((point1, point2))

    return symmetry_lines

def draw_symmetry_lines(image, symmetry_lines):
    # Create a copy of the image to draw on
    output_image = image.copy()
    
    # Draw each line of symmetry
    for (point1, point2) in symmetry_lines:
        cv2.line(output_image, point1, point2, (0, 255, 0), 2)
    
    return output_image

def main(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not read the image.")
        return
    
    # Find the lines of symmetry
    symmetry_lines = find_symmetry_lines(image)
    
    if not symmetry_lines:
        print("No symmetry lines found.")
        return
    
    # Draw the symmetry lines
    output_image = draw_symmetry_lines(image, symmetry_lines)
    
    # Save the new image
    output_path = os.path.join(os.path.dirname(image_path), 'output_with_symmetry_lines.png')
    cv2.imwrite(output_path, output_image)
    
    print(f"Output image saved as: {output_path}")
    # Display the image
    cv2.imshow('Symmetry Lines', output_image)
    
    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main('symmetry\\files\circle.jpg')