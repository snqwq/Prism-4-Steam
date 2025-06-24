import os

# enviornment paths
APPDATA = os.environ.get("APPDATA")
HOMEPATH = os.environ.get("HOMEPATH")

# prism installation paths
WINDOWS_PATH = f"{APPDATA}/PrismLauncher"
SCOOP_PATH = f"{HOMEPATH}/scoop/persist/prismlauncher"
MACOS_PATH = "~/Library/Application Support/PrismLauncher"
LINUX_PATH = "~/.local/share/PrismLauncher"
FLATPAK_PATH = "~/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher"
