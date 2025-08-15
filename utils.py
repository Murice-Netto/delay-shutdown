from pathlib import Path
import platform


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
