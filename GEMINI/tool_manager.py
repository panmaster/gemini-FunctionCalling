import importlib
import os

class ToolManager:
    def __init__(self, tools_dir="tools"):
        self.function_mapping = {}
        self.tool_descriptions = []
        self.load_tools(tools_dir)

    def load_tools(self, tools_dir):
        for filename in os.listdir(tools_dir):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = importlib.import_module(f"{tools_dir}.{module_name}")

                # Get the descriptive dictionary
                description_dict = getattr(module, f"{module_name}_description", None)

                for function_name, function in vars(module).items():
                    if callable(function):
                        self.function_mapping[function_name] = function
                        if description_dict:
                            function_description = description_dict.get("function_declarations", [])[0]
                            if function_description:
                                # Get the description from the dictionary
                                self.tool_descriptions.append({
                                    "name": function_name,
                                    "description": function_description.get("description"),
                                    "parameters": function_description.get("parameters")
                                })