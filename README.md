![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![License](https://img.shields.io/github/license/NCSU-CSC-510-F2024/HW1.svg)
[![HW1 Tests](https://github.com/NCSU-CSC-510-F2024/HW1/actions/workflows/test_hw1.yml/badge.svg?event=push)](https://github.com/NCSU-CSC-510-F2024/Homework/actions/workflows/test_hw1.yml)
[![HW2 Tests](https://github.com/NCSU-CSC-510-F2024/HW1/actions/workflows/test_hw2.yml/badge.svg?event=push)](https://github.com/NCSU-CSC-510-F2024/Homework/actions/workflows/test_hw2.yml)
[![Coverage Status](https://coveralls.io/repos/github/NCSU-CSC-510-F2024/Homework/badge.svg?branch=main)](https://coveralls.io/github/NCSU-CSC-510-F2024/Homework?branch=main)
[![linting: pylint](https://github.com/NCSU-CSC-510-F2024/Homework/actions/workflows/pylint.yml/badge.svg)](https://github.com/NCSU-CSC-510-F2024/Homework/actions/workflows/pylint.yml)
[![security: bandit](https://github.com/NCSU-CSC-510-F2024/Homework/actions/workflows/bandit.yml/badge.svg)](https://github.com/NCSU-CSC-510-F2024/Homework/actions/workflows/bandit.yml)
[![style: autopep8](https://github.com/NCSU-CSC-510-F2024/Homework/actions/workflows/autopep8.yml/badge.svg)](https://github.com/NCSU-CSC-510-F2024/Homework/actions/workflows/autopep8.yml)

# For Virtual Environment Setup

## unix/macOS:

1. if there is no .venv folder run:\
   `python3.13 -m venv .venv`
2. Activate the virtual env:\
   `source .venv/bin/activate`
3. Confirm activation:\
   `which python`
    - Should return a path that ends in:\
      `.venv/bin/python`
4. Prepare pip\
   `python3.13 -m pip install --upgrade pip`\
   `python3.13 -m pip --version`
5. Install packages with requirements.txt\
   `python3.13 -m pip install -r requirements.txt`
6. More info here:\
   [Install packages in a virtual environment using pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

7. To deactivate the virtual environment:\
   `deactivate`
