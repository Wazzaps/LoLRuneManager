import sys
from cx_Freeze import setup, Executable

opts = {
    "packages": ["os", "codecs", "cv2", "numpy"],
    "excludes": ["tkinter"],
    "include_files": [
        "editbtn.png",
        "editbtn_large.png",
        "pathmask.png",
        "runemask.png",
        "Example page 1.txt",
        "Example page 2.txt",
        "README - instructions.txt"
    ]
}

setup(
    name="LoL Rune Manager",
    version="1.0",
    description="LoL Rune Manager",
    options={"build_exe": opts},
    executables=[
        Executable("import.py", base = "Win32GUI", icon="importer_icon.ico"),
        Executable("export.py", base = "Win32GUI", icon="exporter_icon.ico")
    ]
)
