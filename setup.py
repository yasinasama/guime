import sys

from cx_Freeze import setup, Executable

if sys.platform == "win32":
    base = "Win32GUI"
else:
    base = None

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
    executables=executables
)