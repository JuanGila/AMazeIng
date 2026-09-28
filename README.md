1. Makefile
2. pyproject.toml
3. requirements.txt
4. .gitignore
5. config parser
6. representación Cell/Maze
7. MazeGenerator(BFS)
8. PERFECT=True
9. solución BFS(deberia ser Djikstra)
10. output hexadecimal
11. validación
12. PERFECT=False
13. "42"
14. renderer ASCII
15. tests
16. packaging mazegen
17. README
18. revisión final con flake8 + mypy

*This project has been created as part of the 42 curriculum by jgilaber y x.*

# A-Maze-ing

## Description

## Features

## Installation

## Instructions

## Configuration File

### Configuration format

### Configuration parameters

### Example configuration
```text
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=output/maze.txt
PERFECT=True
```

## Maze Generation Algorithm

### Algorithm overview

### Why this algorithm?

## Maze Representation

## Output Format

## Visual Representation

## Reusable Maze Generator

### Installation

### Basic usage

### Custom parameters

### Accessing the maze

### Accessing the solution

## Project Architecture

La arquitectura se divide en varias capas: configuración, generación,
representación del laberinto y salida/consumo del laberinto.

```text
config.txt
    │
    ▼
┌─────────────────┐
│  ConfigParser   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    MazeConfig   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  MazeGenerator  │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
 PERFECT   PLAYABLE
 Generator  Generator
    │         │
    └────┬────┘
         │
         ▼
┌─────────────────────────┐
│          Maze           │
│                         │
│  Cell  Cell  Cell       │
│  Cell  Cell  Cell       │
│  Cell  Cell  Cell       │
└───────────┬─────────────┘
            │
       ┌────┼────┐
       │    │    │
       ▼    ▼    ▼
    Solver Renderer Writer
       │    │    │
       ▼    ▼    ▼
   N E E S  │  maze.txt
            │
      Terminal/MiniLibX
```

## Team and Project Management

### Team roles

### Planning

### What worked well

### What could be improved

### Tools Used

## AI Usage

## Resources

## Advanced Features / Bonuses

## License

MIT License

Copyright (c) 2026 JuanGilabert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# A-Maze-ing

A graphical maze generator written in ¿C? as part of the 42 curriculum.

The project generates mazes according to a set of configurable parameters and provides a visual representation of the generated maze.

## Project

This project was developed as part of the curriculum at **42 Madrid**.

The goal of the project is to practice:

* Python programming
* Algorithm design
* Data structures
* Maze generation
* File parsing and validation
* Error handling
* Graphics / graphical interfaces
* Unit testing

## Usage

Clone the repository and compile the project:

```bash
git clone https://github.com/YOUR_USERNAME/a-maze-ing.git
cd a-maze-ing
make
```

Then run the program according to the project's required arguments:

```bash
./a-maze-ing [arguments]
```

See the source code and project documentation for the available options.

## Structure

```text
.
├── config
├── core
├── dependencies
├── mazegen
├── renderer
├── tests
├── utils
├── .gitignore
├── Makefile
├── includes/
├── src/
└── ...
```

## 42

This repository contains my personal implementation of the A-Maze-ing project developed during my studies at 42 Madrid.

The project specification, subject, evaluation criteria, and other materials provided by 42 are not my original work and remain subject to their respective rights and terms.

This repository is intended primarily as a record of my own work and learning process.

## License

The original code written for this repository is released under the [MIT License](LICENSE.md).

This license applies to my own contributions only. It does not grant any rights to materials, specifications, assets, or other content belonging to 42.

## Disclaimer

This is my personal solution to the A-Maze-ing project at 42 Madrid.
The project subject and materials provided by 42 are not my original work.

## Author

**TU_NOMBRE**

42 Madrid
