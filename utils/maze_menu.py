

class MazeMenu:
    def __init__(self):
        self.options = {
            "1": "Generate Maze",
            "2": "Solve Maze",
            "3": "Display Maze",
            "4": "Exit"
        }

    def display_menu(self):
        print("Maze Menu:")
        for key, value in self.options.items():
            print(f"{key}. {value}")

    def get_user_choice(self):
        choice = input("Enter your choice: ")
        return choice