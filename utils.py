from pathlib import Path
import platform


def get_user_home_folder() -> Path:
    user_os: str = platform.system().lower()
    if user_os not in ("windows", "linux", "darwin"):
        raise Exception(f"OS not supported: {user_os}")
    return Path.home()
