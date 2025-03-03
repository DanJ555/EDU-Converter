from db_manager import *

def exit_cli() -> None:
    """Closes EDU CLI."""
    print("Closing CLI")
    exit(0)

def show_commands() -> None:
    """Shows available commands."""
    print("\nAvailable commands:\n")
    for command, function in COMMANDS.items():
        description = function.__doc__ if function.__doc__ else ""
        print(f" - {command.ljust(10)} {description}")
    print()

def convert(*args) -> None:
    """Handles .txt and .db file conversions."""
    txt_name = None
    db_name = None
    file_type_err = False

    for arg in args:
        if ".txt" in arg:
            txt_name = arg[:-4]
        elif ".db" in arg:
            db_name = arg[:-3]
        else: file_type_err = True

    if file_type_err:
        print("Command convert failed: check your file type extensions.")
    else:
        pass


COMMANDS = {
    "convert": convert,
    "exit": exit_cli,
    "help": show_commands
}

# DARK_BLUE = "\033[34m"
# RESET = "\033[0m"


def main() -> None:
    print("EDU Editor CLI")
    while True:
        input_line = (
            # input(f"{DARK_BLUE}> {RESET}")
            input("> ")
            .strip()
            .lower()
            .split())
        command, *args = input_line

        try:
            COMMANDS[command](*args)
        except KeyError:
            print(f"Unknown command: {command}.\n Enter 'help' to see available commands.")


if __name__ == "__main__":
    main()
