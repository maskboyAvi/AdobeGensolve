<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<h1 align="center">DoodleFix: An Advanced System for Shape Refinement, Symmetry Analysis, and Completion of Complex Doodles</h1>
<div align="center">
  <a href="https://github.com/karthiks373/aegis">
    <img src="assets/AegisLogo.png">
  </a>
  <p>
    Aegis is a smart contract audit and analysis tool powered by artificial intelligence, dedicated to safeguarding your smart contracts from vulnerabilities.
  <br />
    <br />
    <a href="https://youtu.be/7Y2kOU450fU">View Demo</a>
    ·
    <a href="https://github.com/KarthikS373/aegis/issues">Report Bug</a>
    ·
    <a href="https://github.com/KarthikS373/aegis/issues">Request Feature</a>
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
    <li><a href="#detection">Vulnerability Detection</a></li>
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

Aegis is a cutting-edge smart contract audit and analysis tool, empowered by state-of-the-art artificial intelligence, that safeguards your smart contracts against a wide range of vulnerabilities. Traditional security approaches like manually defining patterns are time-consuming, require deep expertise, and struggle to keep up with ever-evolving threats. Aegis leverages the power of deep learning to offer a faster, more comprehensive solution.

Watch demo [here](https://youtu.be/7Y2kOU450fU)

<h3 id="mission"> Mission: </h3>

Our mission is to empower developers of all skill levels with advanced security capabilities, simplifying the process of building robust and trustworthy smart contracts.

<h3 id="valueproposition"> Value Proposition: </h3>

- **AI-powered Vulnerability Detection:** Our robust machine learning model, trained on extensive real-world data, accurately identifies critical vulnerabilities, exceeding the limitations of traditional rule-based approaches.
- **Solidity Expertise:** Aegis seamlessly supports Solidity, the leading language for smart contract development, ensuring compatibility with your existing projects.
- **Actionable Insights and Remediation:** Detailed reports pinpoint vulnerabilities, their severity levels, and offer concrete suggestions for remediation, guiding you towards secure and reliable smart contracts.
- **Effortless Integration:** Aegis integrates seamlessly into your development workflow with a user-friendly command-line interface, minimizing disruption and maximizing efficiency.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="keyfeatures"> Key Features </h2>

- **Advanced Vulnerability Detection:** Identify a broad spectrum of vulnerabilities, including reentrancy, integer overflow, access control issues, and more.
- **Comprehensive Solidity Support:** Analyze and scan your Solidity code for potential threats.
- **Actionable Insights and Remediation:** Receive detailed reports highlighting vulnerabilities, their severity levels, and suggested fixes.
- **Easy Integration:** Seamlessly integrate Aegis into your development workflow with a user-friendly CLI interface.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="builtwith"> Built with </h2>
 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)  ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Huggingface-white?style=for-the-badge)

<h3> Open Source Pre-trained Models: </h3>

- [ResNet18](https://pytorch.org/vision/main/models/generated/torchvision.models.resnet18.html)
- [TheBloke/Llama-2-7B-Chat-GGML](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)
<!--  [AlfredPros/CodeLlama-7b-Instruct-Solidity](https://huggingface.co/AlfredPros/CodeLlama-7b-Instruct-Solidity) -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="detection"> Vulnerability Detection </h2>

Aegis employs a two-stage approach to vulnerability detection, combining the strengths of ResNet-18 and LLAMA 2.

### [ResNet-18](docs/training/ResNetModelTraining.md):

- Acts as the first line of defense, efficiently extracting crucial features from smart contract bytecode.
- Identifies the presence of vulnerabilities with a broad scope, providing an initial assessment.

### [LLAMA 2](docs/training/FinetuningLlama.md):

- Built upon ResNet-18's foundation, leverages fine-tuning and specialized training to pinpoint vulnerable code segments with enhanced precision.
- Goes beyond mere detection, offering actionable guidance for resolving vulnerabilities through targeted suggestions and potential fixes.

### Key Advantages:

- **Precision Boost**: LLAMA 2's targeted approach minimizes false positives and pinpoints relevant areas for attention, saving developers valuable time and effort.
- **Actionable Insights**: Gain practical, code-level recommendations for addressing vulnerabilities, empowering you to effectively secure your smart contracts.
- **Open Datasets and Hallucination Mitigation**: We prioritize responsible AI practices by utilizing publicly available datasets, actively addressing the potential for hallucination in LLAMA 2, and ensuring the accurate identification and remediation of vulnerabilities.

### Detailed Information:

For a deeper understanding of the fine-tuning process, dataset selection, and mitigation strategies, please refer to the comprehensive [documentation](docs/training) provided.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="gettingstarted"> Getting Started </h2>

<h3 id="installation"> Installation Instructions: </h3>

To setup Aegis in your local machine, you need to have the following prerequisites installed on your system:

1. **Python 3.8 or higher:** [Download and install Python](https://www.python.org/downloads/) if you haven't already.

2. **Poetry:** We use Poetry for dependency management. Install it by following the instructions [here](https://python-poetry.org/docs/#installation).

Once you have the prerequisites, you can set up Aegis by following these steps:

1. **Clone the repository:**

   ```
   git clone https://github.com/KarthikS373/aegis.git
   ```

2. **Navigate to the project directory:**
   ```
   cd aegis
   ```
3. **Install dependencies using Poetry:**
   ```
   poetry install
   ```
4. **Activate Virtual Environment:**
   ```
    poetry shell
   ```
5. **Run your first command:**
   ```
   poetry run aegis --help
   ```

For a more detailed setup guide, consult our [documentation](docs/setup.md).

<h3 id="example"> Example Usage: </h3>

To see Aegis in action, check out our demo or refer to the detailed example usage guide in our documentation:

- **Demo:** [Watch the Demo](https://youtu.be/jKpPOpVc6yM)
- **Example Usage Guide:** [Example Usage Guide](docs/examples/examples.md)

Feel free to explore and experiment with the provided examples to understand how to make the most out of Aegis for your projects.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="clicommands"> CLI Commands </h2>

Aegis offers a set of intuitive CLI commands for efficient interaction. Refer to the [documentation](docs/examples/examples.md) for usage examples.

```
compile : compile the solidity code
```

```
documentation : generate documentation for the smart contract
```

```
generate : generate ready to deploy smart contracts
```

```
info : get information about the application
```

```
report : generate a pdf report for the smart contract, summarizing its content, highlighting detected vulnerabilities, and suggesting optimizations
```

```
scan : scan a file or directory for vulnerabilities
```

```
summary : get summary about the smart contract
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="license"> License </h2>

Aegis is licensed under the MIT license. For more information, please see the [LICENSE](LICENSE) file in the repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="contributing"> Contributing </h2>

We welcome contributions! For detailed instructions on how to contribute, please refer to the [Contributing Guide](docs/contributing.md) in our documentation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="team"> Team Members </h2>

- [Aviral Katiyar](https://github.com/maskboyAvi)
- [Darsh Baxi](https://github.com/darshbaxi)
- [Asim](https://github.com/asim)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
