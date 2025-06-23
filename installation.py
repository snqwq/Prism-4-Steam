import os
import subprocess
import config
from sys import platform

prism_installed = False

print(platform)
if platform == "win32":
    prism_installed = os.path.exists(config.WINDOWS_PATH)
    print(f"is prism installed? {prism_installed}")
