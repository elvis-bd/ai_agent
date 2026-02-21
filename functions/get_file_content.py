import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):

    try:
        # print(working_directory)
        # print(file_path)

        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        # print(abs_file_path)
        valid_file_path = (
            os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir
        )
        # print(valid_file_path)

        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

        return content

    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="reads and reutrns the context of a file",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name and directory path of file to read, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
