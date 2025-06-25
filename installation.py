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
        print("prism installed with Scoop")

    else:
        print("cannot find prism install")

elif platform.system() == "Linux":  # TODO add linux support
    print("linux not yet supported because im lazy")

else:
    print("operating system unknown, or we dont support it yet")

# grab all instances
with open()