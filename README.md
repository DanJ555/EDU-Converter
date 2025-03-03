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
