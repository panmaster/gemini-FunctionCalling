import os
from typing import Dict, List  # Import Dict and List

# Define ANSI escape codes for colors
reset = "\033[0m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
bright_black = "\033[90m"
bright_red = "\033[91m"
bright_green = "\033[92m"
bright_yellow = "\033[93m"
bright_blue = "\033[94m"
bright_magenta = "\033[95m"
bright_cyan = "\033[96m"
bright_white = "\033[97m"


def directory_report(path: str = None, summary_file_name: str = "directory_summary.txt",
                    return_type: str = "all") -> str or Dict or List[Dict] or tuple:
    """Generates a report on the directory structure and file contents.

    Args:
        path (str, optional): The path to the directory to report on. Defaults to the current working directory.
        summary_file_name (str, optional): The name of the file to save the summary report. Defaults to "directory_summary.txt".
        return_type (str, optional): The type of report to return. Options are:
            - "all": Returns a tuple containing the complete report string and the file path of the saved report.
            - "structure": Returns a dictionary representing the directory structure.
            - "files": Returns a list of dictionaries, each containing details about a single file.
            - "content": Returns a dictionary with file names as keys and their contents as values.
            - "specific_file": Returns the content of a specific file (not implemented yet).
            - "specific_file_structure": Returns the structure of a specific file (not implemented yet).

    Returns:
        str or Dict or List[Dict] or tuple: The report based on the specified return type.
    """
    print(f"{blue}Entering: directory_report(...)")
    if path is None:
        path = os.getcwd()

    report = {}
    file_list = []
    report_file_path = os.path.join(path, summary_file_name)

    # Generate report recursively
    for root, _, files in os.walk(path):
        # Create directory structure in the report
        current_level = root.replace(path, '').lstrip('/').split('/')
        current_dir = report
        for level in current_level:
            if level not in current_dir:
                current_dir[level] = {}
            current_dir = current_dir[level]

        # Add files to the report
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append({'name': file, 'path': file_path, 'content': ''})
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                current_dir[file] = content

    # Return the report based on the return type
    if return_type == "all":
        report_str = f"Directory report for: {path}\n\n"
        report_str += _format_report(report)
        save_to_file(report_str, summary_file_name, path)
        print(f"{green}Report saved to: {report_file_path}")
        print(f"{blue}Exiting: directory_report(...)")
        return report_str, report_file_path
    elif return_type == "structure":
        print(f"{blue}Exiting: directory_report(...)")
        return report
    elif return_type == "files":
        print(f"{blue}Exiting: directory_report(...)")
        return file_list
    elif return_type == "content":
        print(f"{blue}Exiting: directory_report(...)")
        return {file['name']: file['content'] for file in file_list}
    elif return_type in ("specific_file", "specific_file_structure"):
        print(f"{red}Error: 'specific_file' and 'specific_file_structure' not implemented yet.")
        print(f"{blue}Exiting: directory_report(...)")
        return "Error: 'specific_file' and 'specific_file_structure' not implemented yet."
    else:
        print(f"{red}Invalid return type: {return_type}")
        print(f"{blue}Exiting: directory_report(...)")
        return "Invalid return type."


def _format_report(report: Dict, indent: int = 0, prefix: str = ""):
    """Recursively formats the report dictionary for printing."""
    output = ""
    for key, value in report.items():
        if isinstance(value, dict):
            output += f"{prefix}{' ' * indent}{key}:\n"
            output += _format_report(value, indent + 2, prefix + " " * indent)
        else:
            output += f"{prefix}{' ' * indent}{key}: {value}\n"
    return output


def save_to_file(report_str: str, summary_file_name: str, path: str):
    """Saves the report string to a file."""
    try:
        with open(os.path.join(path, summary_file_name), 'w', encoding='utf-8') as f:
            f.write(report_str)
    except Exception as e:
        print(f"{red}Error saving report to file: {e}")


# Description for function and variables
directory_report_description = {
    'function_declarations': [
        {
            'name': 'directory_report',
            'description': 'Generates a report on the directory structure and file contents.',
            'parameters': {
                'type_': 'OBJECT',
                'properties': {
                    'path': {'type_': 'STRING', 'description': 'The path to the directory to report on. Defaults to the current working directory.'},
                    'summary_file_name': {'type_': 'STRING', 'description': 'The name of the file to save the summary report. Defaults to "directory_summary.txt".'},
                    'return_type': {'type_': 'STRING', 'description': 'The type of report to return. Options are:\n'
                                                                           '- "all": Returns a tuple containing the complete report string and the file path of the saved report.\n'
                                                                           '- "structure": Returns a dictionary representing the directory structure.\n'
                                                                           '- "files": Returns a list of dictionaries, each containing details about a single file.\n'
                                                                           '- "content": Returns a dictionary with file names as keys and their contents as values.\n'
                                                                           '- "specific_file": Returns the content of a specific file (not implemented yet).\n'
                                                                           '- "specific_file_structure": Returns the structure of a specific file (not implemented yet).'}
                },
                'required': []
            }
        }
    ],
    'variable_declarations': [
        {
            'name': 'reset',
            'description': 'Resets the terminal color to the default.'
        },
        {
            'name': 'black',
            'description': 'Sets the terminal text color to black.'
        },
        {
            'name': 'red',
            'description': 'Sets the terminal text color to red.'
        },
        {
            'name': 'green',
            'description': 'Sets the terminal text color to green.'
        },
        {
            'name': 'yellow',
            'description': 'Sets the terminal text color to yellow.'
        },
        {
            'name': 'blue',
            'description': 'Sets the terminal text color to blue.'
        },
        {
            'name': 'magenta',
            'description': 'Sets the terminal text color to magenta.'
        },
        {
            'name': 'cyan',
            'description': 'Sets the terminal text color to cyan.'
        },
        {
            'name': 'white',
            'description': 'Sets the terminal text color to white.'
        },
        {
            'name': 'bright_black',
            'description': 'Sets the terminal text color to bright black.'
        },
        {
            'name': 'bright_red',
            'description': 'Sets the terminal text color to bright red.'
        },
        {
            'name': 'bright_green',
            'description': 'Sets the terminal text color to bright green.'
        },
        {
            'name': 'bright_yellow',
            'description': 'Sets the terminal text color to bright yellow.'
        },
        {
            'name': 'bright_blue',
            'description': 'Sets the terminal text color to bright blue.'
        },
        {
            'name': 'bright_magenta',
            'description': 'Sets the terminal text color to bright magenta.'
        },
        {
            'name': 'bright_cyan',
            'description': 'Sets the terminal text color to bright cyan.'
        },
        {
            'name': 'bright_white',
            'description': 'Sets the terminal text color to bright white.'
        }
    ]
}
