import os


def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    # Will be True or False
    valid_target_dir = (
        os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    )

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        files_list = os.listdir(target_dir)
    except (PermissionError, FileNotFoundError, OSError) as e:
        return f'Error: cannot list "{directory}": {e}'

    dir_contents = ""

    for file in files_list:
        abs_file_loc = os.path.join(target_dir, file)

        try:
            is_dir = os.path.isdir(abs_file_loc)
        except (OSError, PermissionError) as e:
            return f'Error: cannot stat "{file}": {e}'

        size = 0
        if not is_dir:
            try:
                size = int(os.path.getsize(abs_file_loc))
            except (OSError, PermissionError, FileNotFoundError) as e:
                return f'Error: cannot get size for "{file}": {e}'

        populated_file_info = f"- {file}: file_size={size} bytes, is_dir={is_dir}\n"
        dir_contents += populated_file_info
    return dir_contents
