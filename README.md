# AdobeGensolve

## Project Title
**ShapeTransformer**: Transforming Distorted Shapes into Their Closest Real Forms

## Introduction
ShapeTransformer is an innovative tool designed to address the challenge of distorted shapes in images. This project aims to classify distorted shapes into their closest real geometric forms, such as squares, circles, or triangles. If the shape cannot be confidently classified, it remains unchanged. Furthermore, for shapes that are successfully transformed, the tool performs a symmetry check to ensure the transformed shape adheres to geometric symmetry principles. This dual approach of classification and transformation ensures accurate and visually coherent shape representations.

## Configuration
- **Dependencies**:
  - TensorFlow/Keras
  - OpenCV
  - NumPy
  - SciPy
- **Tools**:
  - Python 3.8+
  - Jupyter Notebook (for experimentation)
- **Setup Instructions**:
  1. Clone the repository.
  2. Install required dependencies using `pip install -r requirements.txt`.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ShapeTransformer.git
   cd ShapeTransformer
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Project**:
   - To start the shape classification and transformation process, execute:
     ```bash
     python main.py
     ```
     
## Details
ShapeTransformer consists of two main components:
1. **Shape Classification**:
   - Uses a machine learning model to classify distorted shapes into predefined geometric categories.
2. **Shape Transformation and Symmetry Check**:
   - Transforms classified shapes into their proper geometric forms.
   - Performs a symmetry check on the transformed shapes to ensure geometric integrity.

## Language and Code Explanations
- **Programming Language**: Python
- **Frameworks**:
  - TensorFlow/Keras for shape classification.
  - OpenCV for image processing.
- **Key Concepts**:
  - Machine learning classification using Convolutional Neural Networks (CNNs).
  - Geometric transformation and symmetry analysis.

## Contributors
### 1. [Aviral Katiyar](https://github.com/maskboyAvi)
- **Role**: AI-ML Engineer
- **Responsibilities**: Developed algorithms for shape classification and trained models for accurate shape detection.

### 2. [Darsh Baxi](https://github.com/darshbaxi)
- **Role**: AI-ML Engineer
- **Responsibilities**: Developed shape transformation algorithms and trained a CNN model for accurate shape classification.

### 3. [Asim](https://github.com/asim)
- **Role**: AI-ML Engineer
- **Responsibilities**: Implemented algorithms for symmetry detection in transformed shapes.

## Links
- [Issue Tracker](link-to-issue-tracker)
- [Project Documentation](link-to-project-documentation)
- [Project Homepage](link-to-project-homepage)
- [Project License](link-to-project-license)

---

Feel free to adjust any details as needed!
