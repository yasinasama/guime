import sys

from cx_Freeze import setup, Executable

if sys.platform == "win32":
    base = "Win32GUI"
else:
    base = None

opts = {"include_files": ["db/", "ui/", "utils/"]}


executables = [
    Executable(
        'run.py',
        base=base,
        targetName='guime-app'
    )
]

setup(
    name="guime",
    version="0.2",
    description="guime app",
    author="yasina",
    options={"build_exe": opts},
    executables=executables
)