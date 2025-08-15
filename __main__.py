from pathlib import Path
from utils import (
    get_user_home_folder,
    convert_string_time_to_seconds,
    find_app_file,
    extract_time_from_file_path,
)
from timer import display_timer


FILE_PREFIX: str = "DTF-"


def main():
    base_dir: Path = get_user_home_folder()

    app_file_path: Path = find_app_file(base_dir, FILE_PREFIX)
    time_string: str = extract_time_from_file_path(app_file_path, FILE_PREFIX)
    time_seconds: int = convert_string_time_to_seconds(time_string)

    display_timer(time_seconds)


if __name__ == "__main__":
    main()
