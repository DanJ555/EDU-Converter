# EDU-Converter

EDU-Converter is a command-line utility designed to simplify editing the text-based **export_descr_unit** files used in classic Total War games (such as *Rome* and *Medieval 2*). By converting these files into a SQLite database, users can easily perform mass editing, filtering, and other database operations. Once the edits are complete, the utility can convert the database back into a text file format that the game can read.

---

## Features

- **Text-to-Database Conversion:**  
  Convert complex export_descr_unit text files into an SQLite database to facilitate easier editing and management of unit data.

- **Database Editing:**  
  Leverage SQLite tools to perform mass edits, filter unit data, and more, providing a more robust environment than directly editing text files.

- **Database-to-Text Conversion:**  
  After editing, convert the modified database back into a text file suitable for use in Total War games. The conversion process removes unnecessary lines and comments, preserving the extra name on the dictionary line.

- **Streamlined Workflow:**  
  The CLI provides simple commands to initialize databases, perform conversions, and exit the utility.

---

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/DanJ555/EDU-Converter.git
   cd EDU-Converter
   ```
2. **Dependencies:**  
   Ensure you have **Python 3.9+** installed along with the required dependencies:
   ```sh
   pip install sqlite3
   ```

3. **Files:**  
   The project includes the following key modules:
   - `cli.py`: Main command-line interface for the tool.
   - `db_manager.py`: Handles database creation, data insertion, and extraction.
   - `unit_type.py`: Defines the `Unit` class and its data structure.

---

## Usage

Launch the EDU-Converter CLI by running:

```bash
python cli.py
```

### Available Commands

- **convert:**  
  Converts between a text file and a database file and vice versa.  
  **Usage examples:**
  - Convert text to database:
    ```bash
    convert export_descr_unit.txt export_descr_unit.db
    ```
  - Convert database back to text:
    ```bash
    convert export_descr_unit.db export_descr_unit.txt
    ```

- **initialize:**  
  Initialize a new empty database:
  ```bash
  initialize your_database.db
  ```

- **help:**  
  Display available commands and their usage:
  ```bash
  help
  ```

- **exit:**  
  Exit the CLI:
  ```bash
  exit
  ```

### Database Management

For manual database edits, we recommend using [DB Browser for SQLite](https://sqlitebrowser.org/). This free and open-source tool allows you to view, modify, and commit changes to the database with a graphical interface.

---

## Known Issues

- **Generated File Rejection:**  
  In some cases, the game may reject the text file produced by EDU-Converter. A simple workaround is to copy and paste the generated text into a new file using a basic text editor (such as Notepad) and save it again.

---

## Contributing

Contributions and suggestions are welcome. Feel free to open issues or submit pull requests on the project repository.

---

## License

This project is provided under the GPLv3 License.


# Total War EDU Editor

## Overview

The **Total War EDU Editor** is a Python-based tool that allows modders to efficiently edit and manage unit stats for *Rome: Total War*, *Medieval II: Total War*, *Rome Remastered*, and various mods. By transitioning from text-based `export_descr_unit.txt` (EDU) editing to a structured **SQLite database**, this tool provides a streamlined way to modify, query, and batch-edit unit data.

## Features

- **Convert EDU to SQLite:** Automatically parses `export_descr_unit.txt` into an organized database.
- **Edit Units via CLI:** Modify unit attributes, weapons, armor, and formations directly from the command line.
- **Multiple Database Tables:**
  - `units` → Core unit data.
  - `weapons` → Primary, secondary, and tertiary weapon data.
  - `armor` → Primary and secondary armor stats.
  - `formations` → Unit spacing, morale, fatigue, and charge distance.
- **Ownership & Attributes Parsing:** Stored as comma-separated values, handled via Python.
- **Batch Editing Support:** Modify multiple units at once using SQL queries or CLI commands.

## Installation

### Prerequisites

Ensure you have **Python 3.9+** installed along with the required dependencies:

```sh
pip install sqlite3 argparse
```

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/YourUsername/TotalWar-EDU-Editor.git
   cd TotalWar-EDU-Editor
   ```
2. Initialize the database:
   ```sh
   python cli.py initialize
   ```
3. Convert an EDU file to the database:
   ```sh
   python cli.py convert path/to/export_descr_unit.txt
   ```

## Database Management

For manual database edits, we recommend using [DB Browser for SQLite](https://sqlitebrowser.org/). This free and open-source tool allows you to view, modify, and commit changes to the database with a graphical interface.

## Usage

### Editing Unit Data

Modify a unit’s stat using the CLI:

```sh
python cli.py edit <unit_name> <stat> <value>
```

Example:

```sh
python cli.py edit Dismounted_Feudal_Knights stat_pri_attack 12
```

### Export Changes Back to EDU

Once all edits are made, generate a new `export_descr_unit.txt`:

```sh
python cli.py export path/to/new_export_descr_unit.txt
```

## Planned Features

- **GUI Support**: A graphical interface for easier editing.
- **Batch Edits**: Apply filters and modify multiple units at once.
- **Mod Compatibility**: Auto-detect game version for tailored editing.
- **Validation & Logging**: Catch invalid entries and log changes.

## Contributing

Feel free to submit **issues, feature requests, or pull requests** on GitHub!

## License

MIT License. Free to use and modify.

