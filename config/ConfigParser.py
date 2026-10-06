"""
IV.3 Configuration file format
    The configuration file must contain one ‘KEY=VALUE‘ pair per line.
    Lines starting with # are comments and must be ignored.
    The following keys are mandatory:
        Key         Description                     Example
        WIDTH       Maze width (number of cells)    WIDTH=20
        HEIGHT      Maze height                     HEIGHT=15
        ENTRY       Entry coordinates (x,y)         ENTRY=0,0
        EXIT        Exit coordinates (x,y)          EXIT=19,14
        PERFECT     Is the maze perfect?            PERFECT=True
        OUTPUT_FILE Output filename                 OUTPUT_FILE=maze.txt

    You may add additional keys (e.g., seed, algorithm, display mode) if useful.
    A default configuration file must be available in your Git repository
    
1.- Se comprueba que el fichero de configuracion exista(file not found).
2.- Se comprueba que el fichero de configuracion tenga la sintaxis correcta(bad syntax).
3.- Una vez se ha comprbado que la sintaxis es correcta, verificamos si los parametros indicados por KEY=VALUE son posibles o no(impossible maze parameters)
4.- Una vez se ha comprbado que los parametros son posibles, verificamos si la configuracion es valida o no(invalid configuration).

You may add additional keys (e.g., seed, algorithm, display mode) if useful.
A default configuration file must be available in your Git repository.
"""
from pathlib import Path


class ConfigParser:
    def __init__(self, config_file: str | Path):
        self.config_file: str | Path = config_file
        #self.config = self.parse_config_file()
        self.available_config_keys: list[str] = [
            "WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"
        ]


    # Funcion que comprueba si el fichero de configuracion tiene la sintaxis correcta(bad syntax).
    def check_file_config_syntax(self) -> bool:
        """
        Comprobamos que la sintaxis del fichero se exactamente KEY=VALUE
        donde solo haya un par de KEY=VALUE por linea,
        las claves esten en mayusculas y los valores no esten vacios y no contengan cosas raras como mas = o otros caracteres.

        Tip:
            if not check_file_config_syntax(config_file):
                print(f"Bad syntax in file {config_file}.")
                return False
        """
        with open(self.config_file, "r") as file:
            for line in file:
                if line.startswith("#"):
                    continue
                if "=" not in line:
                    return False
                key, value = line.split("=")
                if not key.isupper() or key not in self.available_config_keys:
                    return False
                if not value:
                    return False
        return True


    # Funcion que comprueba si los parametros indicados por KEY=VALUE son posibles o no(impossible maze parameters)
    def check_maze_parameters(self) -> bool:
        """
        Comprobamos que los parametros tengan realmente sentido,
        ya que el parametro ABCD=1234 es valido en -> check_file_config_syntax
        pero no es valido en -> check_maze_parameters ya que no son parametros de un laberinto

        if not check_maze_parameters(config_file):
            print(f"Impossible maze parameters in file {config_file}.")
            return False
        """
        with open(self.config_file, "r") as file:
            for line in file:
                key, value = line.split("=")
                if key not in self.available_config_keys:
                    return False
        return True


    # Funcion que comprueba si la configuracion es valida o no(invalid configuration). ESTO PODRIA SER INECESARIO AL TENER PYDANTIC.
    def check_maze_configuration(self) -> bool:pass


# Funcion que comprueba si el fichero de configuracion existe(file not found).
def check_config_maze_file(config_file: Path) -> bool:
    if not check_maze_configuration(config_file):
        print(f"Invalid configuration in file {config_file}.")
        return False
    return True



"""
required_keys = {
    "WIDTH",
    "HEIGHT",
    "ENTRY",
    "EXIT",
    "OUTPUT_FILE",
    "PERFECT",
}

missing_keys = required_keys - maze_config.keys()

if missing_keys:
    raise ValueError(
        f"Missing configuration keys: {', '.join(sorted(missing_keys))}"
    )
"""