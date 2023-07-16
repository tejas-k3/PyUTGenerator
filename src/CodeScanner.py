import os
import ast
from UnitTestGenerator import generate_unit_tests
def scan_directory(directory_path, depth):
    """
    Recursively scan a directory and its subdirectories up to a specified depth.
    @directory_path (str): The path of the source directory to scan.
    @depth (int): The maximum depth of subdirectories to traverse.
    @file_paths (list): A list of file paths found within the directory and subdirectories.
    """
    file_paths = []
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        for root, dirs, files in os.walk(directory_path):
            # print(root, dirs, files)
            current_depth = root[len(directory_path) + len(os.path.sep):].count(os.path.sep)
            if current_depth > depth:
                continue
            for file in files:
                file_paths.append(os.path.join(root, file))
    else:
        print("Invalid directory path or directory does not exist.")

    return file_paths

def extract_function_information(file_path):
    """
    Extracts information about the functions present in a Python file.
    @file_path (str): The path of the Python file to extract function information from.
    @function_info_list (list): A list of dictionaries containing function information.
            Each dictionary represents a function and contains keys like 'name', 'parameters', etc.
    """
    function_info_list = []
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            current_class = node.name
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            parameters = [arg.arg for arg in node.args.args]
            # You can extract more information as needed, such as return type, docstring, etc.
            # Add additional keys to the function_info dictionary accordingly.
            function_info = {
                'file_name': file_path,
                'class_name': current_class,
                'name': function_name,
                'parameters': parameters,
                'function_info': node,
            }
            function_info_list.append(function_info)
    
    return function_info_list

# Code to test current file
# if __name__ == "__main__":
# Directory name under the current directory
    # directory_name = "testCode"
    # outputFile = "bazinga"
    # # Get the path of the directory
    # directory_path = os.path.join(os.getcwd(), directory_name)
    # source_directory = directory_path
    # max_depth = 2
    # file_paths = scan_directory(source_directory, max_depth)
    # print(os.listdir())
    # for file in file_paths:
    #     functions = extract_function_information(file)
    #     for function in functions:
    #         print(function)
    #     generate_unit_tests(functions, directory_path+'/output')
    
