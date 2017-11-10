import sys
from cx_Freeze import setup, Executable

opts = {"packages": ["os", "codecs"], "excludes": ["tkinter"], "include_files": ["editbtn.png", "editbtn_large.png"]}

setup(
    name = "LoL Rune Manager",
    version = "1.0",
    description = "LoL Rune Manager",
    options = {"build_exe": opts},
    executables = [Executable("import.py", base = "Win32GUI")])