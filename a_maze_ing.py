"""A-Maze-ing main entry point."""

import sys


def main() -> int:
    """Run the maze generator application.

    Returns:
        Exit status of the application.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return 1
    config_file = sys.argv[1]
    try:
        print(f"Loading configuration: {config_file}")

        # TODO:
        # 1. Load configuration
        # 2. Validate configuration
        # 3. Create MazeGenerator
        # 4. Generate maze
        # 5. Find solution
        # 6. Write output
        # 7. Display maze

    except (OSError, ValueError) as error:
        print(f"Error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())