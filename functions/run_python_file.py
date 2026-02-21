import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        valid_file_path = (
            os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir
        )

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if file_path[-2:] != "py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file_path]

        if args is not None:
            command.extend(args)

        command_run = subprocess.run(
            command, capture_output=True, text=True, timeout=30
        )

        output_string = ""

        return_code = command_run.returncode
        std_out = command_run.stdout
        std_err = command_run.stderr

        if return_code != 0:
            output_string += f"Process exited with code {command_run.returncode}"

        if std_out is not None:
            output_string += f"STDOUT: {std_out}"
        else:
            output_string += "stdout: No output produced"

        if std_err is not None:
            output_string += f"STDERR: {std_err}"
        else:
            output_string += "stderr: No output produced"
        # print(output_string)
        return output_string

    except Exception as e:
        return f"Error executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="runs a python file",
    parameters=types.Schema(
        required=["file_path", "args"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name and directory path of a python file we want to run, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="arguments potentially required by the python file we want to run",
            ),
        },
    ),
)
