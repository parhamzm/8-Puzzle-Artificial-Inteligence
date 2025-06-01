# 8-Puzzle Solver using Artificial Intelligence

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Algorithms Implemented](#algorithms-implemented)
- [File Structure](#file-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---
## Introduction

This project provides a solution to the classic 8-Puzzle problem using various Artificial Intelligence search algorithms. The 8-Puzzle is a sliding puzzle that consists of a frame of 3x3 numbered square tiles in random order with one tile missing. The objective is to reach a goal state (e.g., tiles ordered from 1 to 8) by sliding the tiles.

This repository contains implementations of different search strategies to find the optimal or a near-optimal solution to the 8-Puzzle.

---
## Features

* Solves the 8-Puzzle from a given initial state.
* Implements multiple AI search algorithms.
* Provides a basis for comparing the performance of different search strategies (e.g., path cost, nodes explored, execution time).
* Includes example puzzle inputs (likely in `test3.txt` or similar files).

---
## Algorithms Implemented

Based on the repository's file structure, the following search algorithms are likely implemented:

* **Breadth-First Search (BFS)**: A complete algorithm that guarantees finding the shallowest solution. Several files like `bfs.py`, `bfs_puzzle.py`, etc., suggest its implementation.
* **A\* Search**: An informed search algorithm that uses heuristics to guide the search towards the goal. It aims to find the least-cost path. The `A_Star&Greedy.py` file indicates its presence.
* **Greedy Best-First Search**: An informed search algorithm that expands the node that appears to be closest to the goal, based on a heuristic. This is also suggested by `A_Star&Greedy.py`.

The main logic coordinating these algorithms might be found in `AI_PROJ_8-Puzzle.py`.

---
## File Structure

The repository appears to contain the following key files and types of files:

* `AI_PROJ_8-Puzzle.py`: Likely the main script to run the solver or a central module.
* `A_Star&Greedy.py`: Contains implementations of the A\* and Greedy search algorithms.
* `bfs.py`, `bfs_puzzle.py`, `bfs_Proj.py`, (and other `bfs_*.py` files): Contain implementations of the Breadth-First Search algorithm.
* `test3.txt`: Likely an example input file defining initial puzzle states.
* `.gitignore`: Specifies intentionally untracked files that Git should ignore.
* `LICENSE`: Contains the chosen license for the project.
* `README.md`: This file.

*Users should inspect the individual `.py` files for specific implementation details, class structures, and helper functions.*

---
## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* **Python 3.x**: The project is likely written in Python. Ensure you have a recent version of Python 3 installed.
    ```bash
    python --version
    ```
* **PIP (Python Package Installer)**: Used to install any dependencies.
    ```bash
    pip --version
    ```

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/parhamzm/8-Puzzle-Artificial-Inteligence.git](https://github.com/parhamzm/8-Puzzle-Artificial-Inteligence.git)
    cd 8-Puzzle-Artificial-Inteligence
    ```

2.  **Install dependencies (if any):**
    Check the Python scripts for any `import` statements of external libraries not part of the standard Python library. If found, install them using pip. For example:
    ```bash
    # Example: pip install numpy
    ```
    *At present, specific dependencies are not listed. Please check the source code for imported modules.*

---
## Usage

To run the 8-Puzzle solver, you will likely execute one of the Python scripts from the command line. The main script could be `AI_PROJ_8-Puzzle.py` or individual algorithm files.

**General Steps (Hypothetical):**

1.  **Prepare your input:**
    The puzzle's initial state might be defined in a file (like `test3.txt`) or passed as a command-line argument. The typical format is a 3x3 matrix or a flattened list of 9 numbers, where 0 (or another designated number) represents the empty tile.

    Example `test3.txt` content might look like:
    ```
    1 2 3
    4 0 5
    6 7 8
    ```
    *(Please verify the actual format from your `test3.txt` or input handling code.)*

2.  **Run the solver:**
    You might need to specify the algorithm to use and the input file/state.

    ```bash
    # Example (this is a guess, refer to the code for actual commands):
    # python AI_PROJ_8-Puzzle.py --algorithm A* --input test3.txt
    # OR
    # python A_Star&Greedy.py --input test3.txt
    # OR
    # python bfs_puzzle.py < test3.txt
    ```

3.  **View the output:**
    The solver should output the solution path (sequence of moves or states), the cost of the path, and potentially some performance metrics (e.g., nodes expanded, time taken).

*Please refer to the comments and code within the Python scripts (`AI_PROJ_8-Puzzle.py`, `A_Star&Greedy.py`, `bfs_puzzle.py`, etc.) for the exact command-line arguments, input format, and how to execute the different solvers.*

---
## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.

Please ensure your code adheres to any existing coding style and includes appropriate documentation.

---
## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

**==> IMPORTANT: Please replace `[NAME OF YOUR LICENSE]` above with the actual name of the license you added (e.g., MIT License, Apache License 2.0, GNU GPLv3). <==**

---
