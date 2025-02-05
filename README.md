# Debugging, Static Analysis, and Automated Testing

![Python](https://img.shields.io/badge/Made%20With-Python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Github Repo size in bytes](https://img.shields.io/github/languages/code-size/SE-Spring2025-G2/HW3-Debugging)](https://github.com/SE-Spring2025-G2/HW3-Debugging)
[![Black Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![HW3-Pyflakes](https://github.com/SE-Spring2025-G2/HW3-Debugging/actions/workflows/main.yml/badge.svg)](https://github.com/SE-Spring2025-G2/HW3-Debugging/actions/workflows/main.yml)
[![HW3-Bandit](https://github.com/SE-Spring2025-G2/HW3-Debugging/actions/workflows/bandit.yml/badge.svg)](https://github.com/SE-Spring2025-G2/HW3-Debugging/actions/workflows/bandit.yml)
[![HW3-Pylint](https://github.com/SE-Spring2025-G2/HW3-Debugging/actions/workflows/pylint.yml/badge.svg)](https://github.com/SE-Spring2025-G2/HW3-Debugging/actions/workflows/pylint.yml)
[![HW3-Pytest](https://github.com/SE-Spring2025-G2/HW3-Debugging/actions/workflows/test_workflow.yml/badge.svg)](https://github.com/SE-Spring2025-G2/HW3-Debugging/actions/workflows/test_workflow.yml)

[![Join the Discord Server](https://img.shields.io/badge/Join%20the%20Discord%20Server-7289DA?style=flat&logo=discord&logoColor=white)](https://discord.gg/auXqC4gj)


## Group 2 - Project Members
- **Ayush Pathak** (Unity ID: apathak4)
- **Keyur Gondhalekar** (Unity ID: kbgondha)
- **Ayush Gala** (Unity ID: agala2)

---

## Overview
This repository focuses on implementing debugging best practices and leveraging static analysis tools to improve code quality. The project explores sorting algorithms, random number generation, and solving the N-Queens problem using backtracking. Additionally, automated testing workflows and security analysis tools are integrated for continuous validation.

## Project Structure
```
├── .github/workflows   # CI/CD workflows
├── tests               # Unit tests
├── post_traces         # Static analysis reports
├── hw2_debugging.py    # Sorting algorithms
├── rand.py             # Random number generator
├── nqueens.py          # N-Queens problem solver
├── LICENSE             # License file
├── README.md           # Documentation
├── .gitignore
```
---

## Function Implementations

### `hw2_debugging.py`
This module implements three sorting algorithms:
- **Merge Sort**: Recursively sorts an array using divide-and-conquer.
- **Selection Sort**: Iteratively finds the smallest element and swaps it.
- **Bubble Sort**: Repeatedly swaps adjacent elements to sort the array.

### `rand.py`
A utility module that generates a list of random numbers between 1 and 20 using Python's `secrets` module.

### `nqueens.py`
Solves the **N-Queens problem** using a backtracking algorithm. It ensures that no two queens attack each other and prints solutions in a chessboard format.

---

## ⚙️ Workflows Folder (`.github/workflows`)
This folder contains GitHub Actions workflows for:
- **Static Code Analysis** (`pylint.yml`, `bandit.yml`, `pyflakes`): Identifies code quality issues and security vulnerabilities.
- **Automated Testing** (`test_workflow.yml`): Runs `pytest` to validate implementations.
- Every time someone commits to main, these workflows kick in to validate the programs.

### Tests Folder (`tests`)
Contains unit tests for validating the sorting algorithms. The tests use `pytest` to verify correctness and edge cases. In the future, we will be adding tests for the nqueens solver as well.

---

## Relevant Links
- [Python PDB Debugger](https://docs.python.org/3/library/pdb.html)
- [Pytest Framework](https://pytest.org/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## References
- Guttag, J. V. Introduction to Computation and Programming Using Python.

- Brian Marick, "How to Misuse Code Coverage"

- Ayewah, Pugh, Hovemeyer, Morgenthaler, Penix, "Using Static Analysis to Find Bugs" 

---

## Contributing
We welcome contributions! Follow these steps to contribute:
1. **Fork the repository** on GitHub.

2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/your-username/HW3-Debugging.git
   ```
3. **Create a new branch** for your feature/fix:
   ```bash
   git checkout -b feature-branch
   ```
4. **Make your changes and commit them**:
   ```bash
   git commit -m "Add new feature"
   ```
5. **Push your branch to GitHub**:
   ```bash
   git push origin feature-branch
   ```
6. **Submit a pull request** to merge your changes.

### Issue Reporting
If you find any bugs or have suggestions, feel free to [open an issue](https://github.com/SE-Spring2025-G2/HW3-Debugging/issues).


