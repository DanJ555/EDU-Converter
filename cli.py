from db_manager import *
from os import remove


def exit_cli() -> None:
    """Closes EDU CLI."""
    print("Closing CLI")
    exit(0)


def show_commands(*command) -> None:
    """Shows available commands. Pass a command as an argument for more details."""
    try:
        if command[0] == "convert":
            print("""
Convert takes two arguments, an edu.txt and an edu.db. Example syntax:

    convert export_descr_unit.txt export_descr_unit.db
    
This example will find the specified text file and create a database file with the given name, overwriting
any previous file with the same name. These arguments may also be reversed, to take a database file after
editing unit data and turn it back into a text file.
        """)
        else:
            print("Argument not supported.")
            show_commands()
    except IndexError:
        print("\nAvailable commands:\n")
        for command, function in COMMANDS.items():
            description = function.__doc__ if function.__doc__ else ""
            print(f" - {command.ljust(15)} {description}")
        print()


def convert(*args) -> None:
    """Handles edu.txt and edu.db file conversions. Use help to learn more."""

    if ".txt" in args[0] and ".db" in args[1]:
        try:
            remove(args[1])
        except FileNotFoundError:
            pass
        unit_list = create_units_from_txt(args[0])
        db = open_database(args[1], unit_list)
        db.close()
        print(f"{args[0]} successfully converted to {args[1]}")
    elif ".txt" in args[1] and ".db" in args[0]:
        db = open_database(args[0])
        db_unit_list = extract_units(db)
        create_edu_file(db_unit_list, args[1])
        db.close()
        print(f"{args[0]} successfully converted to {args[1]}")
    else:
        print("Command failed: bad arguments.")


def init(db_name):
    """Initializes a database with no rows input yet."""
    db = initialize_database(db_name)
    db.close()


COMMANDS = {
    "convert": convert,
    "initialize": init,
    "exit": exit_cli,
    "help": show_commands
}


def main() -> None:
    print("EDU Editor CLI")
    while True:
        input_line = (
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
