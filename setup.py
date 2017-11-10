import sys
from cx_Freeze import setup, Executable

opts = {"packages": ["os", "codecs"], "excludes": ["tkinter"], "include_files": ["editbtn.png"]}

setup(
    name = "Roons",
    version = "1.0",
    description = "Roons",
    options = {"build_exe": opts},
    executables = [Executable("import.py", base = "Win32GUI")])