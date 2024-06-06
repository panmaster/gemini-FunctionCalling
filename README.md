Just create  python script  like  save_to_file.py
put  it  to folder: tools

 create funcion and   create function_description : 

< import  os
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



def save_to_file(content: str = None, file_name: str = 'NoName', file_path: str = None):
    print(f"{blue}Entering: save_to_file(...)")
    """Saves content to a file and returns detailed execution result.

    Args:
        content (str): The content to save.
        file_name (str, optional): The name of the file. Defaults to 'NoName'.
        file_path (str, optional): The path to save the file. Defaults to the current working directory if not provided.

    Returns:
        dict: A dictionary containing the status, message, and file path if successful.
    """
    if content is None:
        content = ""
    if file_path is None:
        full_path = os.path.join(os.getcwd(), file_name)
    else:
        full_path = os.path.join(file_path, file_name)

    try:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

        success_message = f"File saved successfully at: {full_path}"
        print(f"{green}{success_message}")
        print(f"{blue}Exiting: save_to_file(...)")
        return {"status": "success", "message": success_message, "file_path": full_path}

    except Exception as e:
        error_message = f"Failed to save file: {str(e)}"
        print(f"{red}{error_message}")
        print(f"{blue}Exiting: save_to_file(...)")
        return {"status": "failure", "message": error_message}





save_to_file_description = {
    'function_declarations': [
        {
            'name': 'save_to_file',
            'description': 'Saves content to a file.',
            'parameters': {
                'type_': 'OBJECT',
                'properties': {
                    'content': {'type_': 'STRING'},
                    'file_name': {'type_': 'STRING', 'description': 'The name of the file. Defaults to "NoName".'},
                    'file_path': {'type_': 'STRING',
                                  'description': 'The path to save the file. Defaults to the current working directory if not provided.'}
                },
                'required': []
            }
        }
    ]
}>
