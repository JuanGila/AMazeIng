"""
test_config.py
│   ├── configuración válida
│   ├── configuración incompleta
│   ├── valores inválidos
│   └── coordenadas inválidas
"""


def test_valid_config():
    pass


def test_incomplete_config():
    pass


def test_invalid_values():
    pass


def test_invalid_coords():
    pass

def test_config():
    test_valid_config()
    test_incomplete_config()
    test_invalid_values()
    test_invalid_coords()


if __name__ == "__main__":
    try:
        test_config()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"{base_err.__class__.__name__}: {base_err}\n")
