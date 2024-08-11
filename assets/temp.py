from PIL import Image

def resize_image(input_path, output_path, size):
    
    with Image.open(input_path) as img:
        resized_img = img.resize(size)
        resized_img.save(output_path)
        print(f"Image saved to {output_path} with size {size}")

# Example usage:
input_path = 'star_symm.png'
output_path = input_path
size = (300, 300)  # Width, Height

resize_image(input_path, output_path, size)
