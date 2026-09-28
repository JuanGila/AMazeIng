"""
test_generator.py
│   ├── seed reproducible
│   ├── diferentes seeds
│   └── solución
"""


def test_reproducible_seed():
    pass


def test_diferents_seeds():
    pass


def test_solution():
    pass


def test_generator():
    test_reproducible_seed()
    test_diferents_seeds()
    test_solution()


if __name__ == "__main__":
    try:
        test_generator()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"{base_err.__class__.__name__}: {base_err}\n")
