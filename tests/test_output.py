"""
test_output.py
    ├── formato
    ├── hexadecimal
    └── lectura posterior
"""


def test_hexadecimal_output():
    pass


def test_output():
    test_hexadecimal_output()


if __name__ == "__main__":
    try:
        test_output()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"{base_err.__class__.__name__}: {base_err}\n")
