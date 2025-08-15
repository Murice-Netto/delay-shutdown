from pathlib import Path
import platform
import re


DEFAULT_FOLDERS: list[str] = ["Documents", "Downloads", "Music", "Pictures", "Videos"]


def get_user_home_folder() -> Path:
    user_os: str = platform.system().lower()
    if user_os not in ("windows", "linux", "darwin"):
        raise Exception(f"OS not supported: {user_os}")
    return Path.home()


def find_app_file(
    base_dir: Path, file_prefix: str, folders: list[str] = DEFAULT_FOLDERS
) -> Path:
    for folder in folders:
        folder_path: Path = base_dir / folder
        if not folder_path.exists() or not folder_path.is_dir():
            continue
        for file_path in folder_path.iterdir():
            if file_path.is_file() and file_path.name.startswith(file_prefix):
                return file_path
    raise FileNotFoundError(
        f"File with prefix '{file_prefix}' was not found in {folders}"
    )


def extract_time_from_file_path(file_path: Path, file_prefix: str) -> str:
    return file_path.name.split(file_prefix)[1].split(".")[0]


def match_regex(text: str, reges: str) -> int:
    match = re.search(reges, text)
    return int(match.group(1) if match else 0)


def convert_string_time_to_seconds(text_time: str) -> int:
    hours: int = match_regex(text_time, r"(\d+)h")
    minutes: int = match_regex(text_time, r"(\d+)m")
    seconds: int = match_regex(text_time, r"(\d+)s")
    return hours * 3600 + minutes * 60 + seconds
