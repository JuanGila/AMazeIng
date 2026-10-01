from pydantic import BaseModel, Field
from pydantic import model_validator, ValidationError

class MazeConfig(BaseModel):
    """
    Example:
        WIDTH=20
        HEIGHT=15
        ENTRY=0,0
        EXIT=19,14
        OUTPUT_FILE=output/maze.txt
        PERFECT=True
    """
    def __init__(self, width=10, height=10, complexity=0.75, density=0.75):
        width: int = Field(ge=0, description="Width of the maze")
        height: int = Field(ge=0, description="Height of the maze")
        entry: tuple[int, int] = Field(min_length=1, max_length=2)
        exit: tuple[int, int] = Field(min_length=1, max_length=2)
        output_file: str = Field(min_length=5)#"output/maze.txt"
        perfect: bool = False
        complexity: float = Field(ge=0.0)#revisar si tiene que haber un maximo, supongo que seria 1.0 ¿?
        density: float = Field(ge=0.0)#revisar si tiene que haber un maximo, supongo que seria 1.0 ¿?

        @model_validator(mode="before")
        def validator(self) -> MazeConfig:
            if type(self.width) is bool or type(self.height) is bool:
                raise ValueError("Width or Height must has to be a int.")
            # Verificar los valores de la tupla entry
            # Verificar los valores de la tupla exit
            return self

    def __str__(self):
        return f"MazeConfig(width={self.width}, height={self.height}, complexity={self.complexity}, density={self.density})"