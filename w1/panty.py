# Main Function
from rich.traceback import install
from src.s1 import wo1

install(show_locals=True)


def main():
    wo1()


if __name__ == "__main__":
    main()
