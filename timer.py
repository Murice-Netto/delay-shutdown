import os
import platform


def add_zero_start(value: int) -> str:
    return str(value).rjust(2, "0")


def shutdown() -> None:
    user_os: str = platform.system().lower()
    try:
        if user_os == "windows":
            os.system("shutdown /s /t 0")
        elif user_os in ("darwin", "linux"):
            os.system("sudo shutdown now")
        else:
            raise RuntimeError(f"OS not supported: {user_os}")
    except Exception as e:
        print(f"Failed to shutdown: {e}")
