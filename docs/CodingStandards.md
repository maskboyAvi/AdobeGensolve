## Coding Standards

When contributing to DoodleFix, please adhere to the following coding standards to ensure consistency and readability throughout the codebase.

### Python Version

- Use Python 3.9 or higher for development.

### Code Formatting

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.
- Use 4 spaces for indentation.
- Limit all lines to a maximum of 79 characters for code and 72 for docstrings.

### Naming Conventions

- Use descriptive and meaningful names for variables, functions, classes, and modules.
- Follow the `snake_case` naming convention for functions and variables.
- Follow the `CamelCase` naming convention for classes.

### Imports

- Use absolute imports rather than relative imports.
- Avoid wildcard imports (`from module import *`).
- Group imports in the following order:
  1. Standard library imports.
  2. Related third-party imports.
  3. Local application/library specific imports.

### Comments

- Write clear and concise comments. Comments should explain why, not what (unless the code is particularly complex).
- Avoid unnecessary comments if the code is self-explanatory.

### Docstrings

- Include docstrings for all modules, classes, and public methods/functions.
- Follow the [Google Style Python Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) format.

### Exception Handling

- Only catch exceptions that you can handle effectively.
- Avoid using a bare `except` clause.

### Testing

- Write unit tests for your code using a testing framework such as `pytest`.
- Ensure that all tests pass before submitting a pull request.

### Version Control

- Commit messages should be clear, concise, and written in the present tense.
- Follow the [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) format for commit messages.

### Continuous Integration

- Ensure that your changes pass all CI checks before submitting a pull request.

Adhering to these coding standards will help maintain a clean and cohesive codebase. Thank you for contributing to DoodleFix!