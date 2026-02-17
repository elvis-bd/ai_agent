import os


def write_file(working_directory, file_path, content):
    try:
        # print(working_directory)
        # print(file_path)

        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        # print(abs_file_path)
        valid_file_path = (
            os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir
        )

        if not valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        file_parent_dir = os.path.dirname(abs_file_path)

        if file_parent_dir:
            os.makedirs(file_parent_dir, exist_ok=True)

        with open(abs_file_path, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {e}"
