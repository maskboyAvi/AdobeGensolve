import cv2
import numpy as np

def is_symmetric(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Unable to read image")
        return False
    
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print("No contours found!")
        return False
    
    contour = max(contours, key=cv2.contourArea)
    
    x, y, w, h = cv2.boundingRect(contour)

    object_roi = thresh[y:y+h, x:x+w]

    flipped = cv2.flip(object_roi, 1)

    difference = cv2.absdiff(object_roi, flipped)

    non_zero_count = np.count_nonzero(difference)
    total_pixels = object_roi.size
    percentage_difference = (non_zero_count / total_pixels) * 100

    if percentage_difference < 5:  
        print("The object is symmetric")
        return True
    else:
        print("The object is not symmetric")
        return False

image_path = 'symmetry/files/square.jpg'
is_symmetric(image_path)
