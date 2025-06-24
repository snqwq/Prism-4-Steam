import os
import pathlib
import subprocess
import config
import platform
import pathlib

prism_installed = False


if platform.system() == "Windows":
    if pathlib.Path(config.WINDOWS_PATH).exists():
        prism_installed = True
    elif pathlib.Path(config.SCOOP_PATH).exists():
        prism_installed = True
    else:
        print("cannot find prism install")
    print(f"is prism installed? {prism_installed}")
