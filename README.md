# Domain Engineering Repository

This repository is used for domain engineer assets and workflows.

## Prerequisite:

[Node.js](https://nodejs.org/en): It requires node.js version 18.x.

[Git](https://git-scm.com/): Git should be installed on the machine.

## Local Build Guidelines

1. Clone the repository and navigate to its path through Command Line.
2. Install the preprocessor globally using the following command:
   ```
   npm install -g c-preprocessor
   ```
3. Set environment variables `COMPONENT` and `VARIANT_TYPE` for building the required component's variant.
4. Execute `prepareExecutePreprocessor.py` to prepare the required variant.
5. Now go to the "README.md" file of that component for further build instructions.
