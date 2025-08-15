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


def get_hours_minutes_seconds(total_seconds: int) -> list[int]:
    hours: int = total_seconds // 3600
    minutes: int = (total_seconds % 3600) // 60
    seconds: int = total_seconds % 60
    return [hours, minutes, seconds]


def get_hours_minutes_seconds_divmod(total_seconds: int) -> list[int]:
    hours, remaining_seconds = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)
    return [hours, minutes, seconds]
