<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<h1 align="center">DoodleFix: An Advanced System for Shape Refinement, Symmetry Analysis, and Completion of Complex Doodles</h1>
<div align="center">
  <a href="https://github.com/yourusername/doodlefix">
    <img src="assets/DoodleFixLogo.png" alt="DoodleFix Logo">
  </a>
  <p>
    DoodleFix transforms distorted shapes into their closest geometric forms and ensures symmetry in the refined shapes.
  <br />
    <br />
    <a href="https://youtu.be/your-demo-link">View Demo</a>
    ·
    <a href="https://github.com/yourusername/doodlefix/issues">Report Bug</a>
    ·
    <a href="https://github.com/yourusername/doodlefix/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary><h2> Table of Contents </h2></summary>
  <ol>
    <li>
      <a href="#abouttheproject"> About The Project </a>
      <ul>
        <li><a href="#mission"> Mission </a></li>
        <li><a href="#valueproposition"> Value Proposition </a></li>
      </ul>
    </li>
    <li><a href="#keyfeatures">Key Features</a></li>
    <li><a href="#builtwith">Built With</a></li>
    <li><a href="#detection">Shape Classification and Transformation</a></li>
    <li>
      <a href="#gettingstarted">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation Instructions</a></li>
        <li><a href="#example">Example Usage</a></li>
      </ul>
    </li>
    <li><a href="#clicommands">CLI Commands</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#team">Team Members</a></li>
  </ol>
</details>

<h2 id="abouttheproject"> About the Project </h2>

DoodleFix is a state-of-the-art tool designed to handle distorted shapes by first classifying them into their closest geometric forms, and then transforming them accordingly. If a shape cannot be classified, it remains unchanged. For classified shapes, DoodleFix refines them to their correct geometric forms and performs a symmetry check to ensure they adhere to geometric principles.

Watch demo [here](https://youtu.be/your-demo-link)

<h3 id="mission"> Mission: </h3>

Our mission is to provide a powerful tool for transforming and analyzing distorted shapes, making it easier to work with imperfect or incomplete doodles and ensuring accurate geometric representation.

<h3 id="valueproposition"> Value Proposition: </h3>

- **Shape Classification and Transformation:** Accurately classify distorted shapes into geometric forms and transform them to their proper representations.
- **Symmetry Analysis:** Ensure that transformed shapes adhere to geometric symmetry principles.
- **User-Friendly:** Simplify the process of shape refinement and analysis with an easy-to-use interface.
- **Advanced Algorithms:** Leverage cutting-edge machine learning models to achieve high accuracy in shape classification and transformation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="keyfeatures"> Key Features </h2>

- **Distorted Shape Classification:** Identify if a distorted shape can be classified into a geometric form.
- **Geometric Transformation:** Transform classified shapes into their proper geometric representations.
- **Symmetry Check:** Analyze transformed shapes for symmetry in various directions.
- **Robust Performance:** Handle a wide range of distorted shapes with high accuracy.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="builtwith"> Built with </h2>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-%23FF6F00.svg?style=for-the-badge&logo=OpenCV&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-%2300CFFF.svg?style=for-the-badge&logo=NumPy&logoColor=white)

<h3> Key Libraries: </h3>

- [TensorFlow](https://www.tensorflow.org/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="detection"> Shape Classification and Transformation </h2>

DoodleFix utilizes advanced machine learning models to handle shape classification, transformation, and symmetry checking.

### Shape Classification and Transformation:

- **Shape Classification:** A machine learning model classifies distorted shapes into geometric categories.
- **Geometric Transformation:** Transforms shapes to their proper geometric forms if classified successfully.
- **Symmetry Check:** Analyzes the transformed shapes to ensure geometric symmetry.

### Key Advantages:

- **High Accuracy:** Leveraging advanced models for precise classification and transformation.
- **Versatile Symmetry Analysis:** Check for symmetry in various directions, not limited to vertical and horizontal.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="gettingstarted"> Getting Started </h2>

<h3 id="installation"> Installation Instructions: </h3>

To set up DoodleFix on your local machine, follow these steps:

1. **Python 3.8 or higher:** [Download and install Python](https://www.python.org/downloads/) if you haven't already.

2. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/doodlefix.git
   ```

3. **Navigate to the project directory:**
   ```
   cd doodlefix
   ```

4. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```
   python main.py
   ```

For more detailed setup instructions, refer to our [documentation](docs/setup.md).

<h3 id="example"> Example Usage: </h3>

To see DoodleFix in action, check out our demo or refer to the detailed example usage guide:

- **Demo:** [Watch the Demo](https://youtu.be/your-demo-link)
- **Example Usage Guide:** [Example Usage Guide](docs/examples/examples.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="clicommands"> CLI Commands </h2>

DoodleFix provides a set of CLI commands for efficient interaction. Refer to the [documentation](docs/examples/examples.md) for usage examples.

```
classify : Classify a distorted shape into its closest geometric form
```

```
transform : Transform a classified shape into its proper geometric representation
```

```
check-symmetry : Check if the transformed shape adheres to symmetry principles
```

```
info : Get information about the application
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="license"> License </h2>

DoodleFix is licensed under the MIT license. For more information, please see the [LICENSE](LICENSE) file in the repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="contributing"> Contributing </h2>

We welcome contributions! For detailed instructions on how to contribute, please refer to the [Contributing Guide](docs/contributing.md) in our documentation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="team"> Team Members </h2>

- [Aviral Katiyar](https://github.com/maskboyAvi)
- [Darsh Baxi](https://github.com/darshbaxi)
- [Asim](https://github.com/asim)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

You can adjust the content, images, and links according to your actual project details.
