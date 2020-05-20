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
        targetName='维修记账软件.exe'
    )
]

setup(
    name="维修记账软件",
    version="0.2",
    description="维修记账软件",
    author="yasina",
    executables=executables
)