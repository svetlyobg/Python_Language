import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf']
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name ="Lottery 6/49",
      version="tiraj50",
      description="Lettery Bulgaria",
      options = {'build_exe':{'include_files':include_files}},
      executables = [Executable('Lists.py', base = base)])
