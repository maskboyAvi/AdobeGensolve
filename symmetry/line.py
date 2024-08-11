import cv2
import numpy as np

def draw_line_of_symmetry(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load the image from {image_path}")
        return
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply edge detection
    edges = cv2.Canny(gray, 100, 200)
    
    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate over the contours
    for cnt in contours:
        # Calculate the moments of the contour
        M = cv2.moments(cnt)
        
        # Calculate the centroid of the contour
        if M['m00'] == 0:  # Check to avoid division by zero
            continue
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
        # Calculate the angle of the line of symmetry
        angle = cv2.fitEllipse(cnt)[2]
        
        # Draw the line of symmetry spanning the entire height of the image
        height, width = image.shape[:2]
        pt1 = (cx, 0)  # Start point at the top of the image
        pt2 = (cx, height)  # End point at the bottom of the image
        image = cv2.line(image, pt1, pt2, (0, 255, 0), 2)
    
    # Save the image with the line of symmetry
    output_path = image_path.replace('.', '_output.')
    cv2.imwrite(output_path, image)
    
    print(f"Output image saved as: {output_path}")

# Example usage
draw_line_of_symmetry('star.png')