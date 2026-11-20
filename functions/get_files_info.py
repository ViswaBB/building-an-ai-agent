
import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        # Get absolute working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Construct target directory path
        target_dir = os.path.normpath(
            os.path.join(working_dir_abs, directory)
        )

        # Validate that target is inside working directory
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir])
            == working_dir_abs
        )

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check whether target is a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # Successful validation
        return f'Success: "{directory}" is within the working directory'

    except Exception as e:
        return f"Error: {e}"
