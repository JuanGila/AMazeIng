

class MazeMenu:
    def __init__(self):
        self.options: dict[str, str] = {
            "1": "Generate Maze",
            "2": "Solve Maze",
            "3": "Display Maze",
            "4": "Entry Point",
            "5": "Exit Point",
            "6": "42 Pattern",
            "7": "Shortest Path",
            "8": "Exit Program",
        }

    def display_menu(self):
        print("Maze Menu:")
        for key, value in self.options.items():
            print(f"{key}. {value}")

    def get_user_choice(self):
        choice = input("Enter your choice: ")
        return choice