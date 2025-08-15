# Definir prefixo
# Buscar o arquivo -> Retornar o path
# Arrancar o tempo do path
# Converter o tempo para segundos
# Criar um display do tempo -> Recarrega no terminal
# Criar função para desligar o PC com um loop

import os
import platform
import re
import time


FILE_PREFIX: str = "DTF-"
DEFUALT_FOLDERS: list[str] = ["Documents", "Downloads", "Music", "Pictures", "Videos"]
ABORT_SIGNAL: bool = False
USER_OS: str = platform.system().lower()


def find_app_file(base_dir: str, file_prefix: str, folders: list[str]) -> str:
    for folder in folders:
        current_folder: str = os.path.join(base_dir, folder)
        files: list[str] = os.listdir(current_folder)
        for file in files:
            file_path: str = os.path.join(base_dir, folder, file)
            if os.path.isfile(file_path) and file.startswith(file_prefix):
                return file_path
    raise Exception("file not found")


def get_user_home_folder() -> str:
    if USER_OS == "windows":
        return os.environ["USERPROFILE"]
    elif USER_OS == "darwin" or USER_OS == "linux":
        return os.environ["HOME"]
    else:
        raise Exception("failed to find out user's OS")


def extract_time_from_file_path(file_path: str, file_prefix: str) -> str:
    return file_path.split(file_prefix)[1].split(".")[0]


def convert_string_time_to_seconds(text_time: str) -> int:
    hours: int = int(match_regex(text_time, r"(\d+)h"))
    minutes: int = int(match_regex(text_time, r"(\d+)m"))
    seconds: int = int(match_regex(text_time, r"(\d+)s"))
    return hours * 3600 + minutes * 60 + seconds


def match_regex(text: str, regex: str) -> str:
    match = re.search(regex, text)
    if match:
        return match.group(1)
    else:
        # Mudar isso, está muito gambiarrento
        return "0"


def display_timer(time_seconds: int, abort_signal: bool) -> None:
    print("Press CTRL+C to abort shutdown")
    for remaninig in range(time_seconds, -1, -1):
        try:
            if abort_signal:
                return
            seconds: int = remaninig % 60
            total_minutes: int = remaninig // 60
            minutes: int = total_minutes % 60
            hours: int = total_minutes // 60
            timer_strucutre: str = f"\rShuting down in: {add_zero_start(hours)}:{add_zero_start(minutes)}:{add_zero_start(seconds)}"
            print(timer_strucutre, end="", flush=True)
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutdown Aborted.")
            abort_signal = True
    shutdown()


def main():
    base_dir: str = get_user_home_folder()

    app_file_path: str = find_app_file(base_dir, FILE_PREFIX, DEFUALT_FOLDERS)
    time_string: str = extract_time_from_file_path(app_file_path, FILE_PREFIX)
    time_seconds: int = convert_string_time_to_seconds(time_string)

    display_timer(time_seconds, ABORT_SIGNAL)


if __name__ == "__main__":
    main()
