"""A-Maze-ing main entry point."""

"""
IV.2 Usage
    Your program must be run with the following command:
        python3 a_maze_ing.py config.txt
    •a_maze_ing.py is your main program file. You must use this name.
    •config.txt is the only argument. It is a plain text file that defines the maze
    generation options. You can use a different filename.
    
    Your program must handle all errors gracefully: invalid configuration, file not found, bad
    syntax, impossible maze parameters, etc. It must never crash unexpectedly, and must
    always provide a clear error message to the user.

"""

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

    except (OSError, ValueError, Exception) as error:
        print(f"Error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except SystemExit as sys_exit:
        print(f"\nProgram exited with status {sys_exit.code}.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    except BaseException as base_exception:
        print(f"\nAn unexpected error occurred: {base_exception}")