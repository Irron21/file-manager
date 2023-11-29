# File Manager Project

This Python-based file manager script provides functionality to organize files within a directory automatically. It includes two main features:

1. **Sorting Existing Files:**
    - The script initially organizes the existing files in the specified directory based on their file extensions.
    - It categorizes files into respective subdirectories, one for each file type.

2. **Real-time File Sorting:**
    - Monitors the specified directory for any new file additions.
    - Automatically sorts newly added files into their corresponding directories based on their file extensions.
    - Handles scenarios where files with the same name already exist in the destination directory by renaming the new files.

## Setup and Usage

### Prerequisites

- Python 3.x installed on your system.
- Required Python libraries can be installed via `pip` using the following command:
    ```
    pip install watchdog
    ```

### How to Use

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/file-manager.git
    ```

2. **Run the Script:**
    - Open a terminal or command prompt.
    - Navigate to the directory where the script is located.
    - Execute the following command:
        ```bash
        python file_manager.py
        ```
    - Enter the path of the directory you want to manage when prompted.

3. **Functionality:**
    - The script will organize existing files into respective directories based on their extensions.
    - Any new files added to the watched directory will be immediately sorted into the appropriate subdirectories.

### Notes

- Ensure that the script has necessary permissions to create directories and move files within the specified directory.
- The script handles cases where file conflicts (files with the same name) arise in the destination directory by renaming the newly added files.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).
