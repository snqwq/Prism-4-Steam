from gettext import install
import os
import pathlib
import subprocess
import config
import platform
import pathlib
import json

prism_installed = False
install_path = ""

# system checking
if platform.system() == "Windows":
    if pathlib.Path(config.WINDOWS_PATH).exists():
        prism_installed = True
        install_path = config.WINDOWS_PATH
        print("prism installed")

    elif pathlib.Path(config.SCOOP_PATH).exists():
        prism_installed = True
        install_path = config.SCOOP_PATH
        print("prism installed with Scoop")

    else:
        print("cannot find prism install")

elif platform.system() == "Linux":  # TODO add linux support
    print("linux not yet supported because im lazy")
    exit(0)

else:
    print("operating system unknown, or we dont support it yet")
    exit(0)

# grab all instances
try:
    with open(f"{install_path}/instances/instgroups.json", mode="r") as file:
        data = json.load(file)


except PermissionError:
    print("insufficient permissions to access file")
