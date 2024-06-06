# -*- coding: utf-8 -*-
import google.generativeai as genai
genai.configure(api_key=' your key')
from GEMINI_IMPROVED import tool_manager as tool_manager

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











model = genai.GenerativeModel(
    system_instruction="You are a helpful assistant. Never use emojis. You can save files using functions!",
    model_name='gemini-1.5-pro-latest',
    safety_settings={'HARASSMENT': 'block_none'},

)

def interpreter(response,My_function_Mappings):
    print(f"{bright_yellow}----------------INTERPRETER START----------------------")
    """
    Interprets the model's response, extracts function details,
    and executes the appropriate function with the provided arguments.
    """

    Multiple_ResultsOfFunctions_From_interpreter = []

    if response.candidates:
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'function_call'):
                function_call = part.function_call
                function_name = function_call.name
                function_args = function_call.args

                # Use the ToolManager to get the function
                function_to_call = My_function_Mappings.get(function_name)
                print(f"FUNCTION CALL: {function_name}({function_args}) ")

                try:
                    results = function_to_call(**function_args)
                except TypeError as e:
                    results = f"TypeError: {e}"
                except Exception as e:
                    results = f"Exception: {e}"

                print(f"{bright_blue}Function Call Exit: {function_name}")

                function_name_arguments = f"{function_name}({function_args})"

                modified_results = f"Result of Called function {function_name_arguments}: {results}"
                Multiple_ResultsOfFunctions_From_interpreter.append(modified_results)

    print(f"{bright_yellow}----------------INTERPRETER END------------------------")
    print()
    return Multiple_ResultsOfFunctions_From_interpreter



chat1 = model.start_chat(history=[])




while True:
    user_input = input(f"{bright_green}user: {reset}")

    try:
        import  tool_manager as tool_manager
        TOOLS=tool_manager.ToolManager()
        MyTools=TOOLS.tool_descriptions
        print(MyTools)
        My_function_Mappings=TOOLS.function_mapping
        print(My_function_Mappings)


        response = chat1.send_message(user_input,tools=MyTools)
        print(f"{bright_magenta}Model Response: {response}")
        try:
            results = interpreter(response,My_function_Mappings)
            print(f"{bright_cyan}Results of Interpreter and Called Functions: {results}")
        except Exception as e:
            print(f"{bright_red}Error with interpreter: {e}")
    except Exception as e:
        print(f"{bright_red}An error occurred: {e}")


print(f"{bright_yellow}Exiting the program.")