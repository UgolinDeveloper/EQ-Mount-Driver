# + ------------------------------------------------- + #
# | File    : launcher.py                             | #
# | Author  : UgolinDeveloper / Matthieu              | #
# | Date    : 09/11/20                                | #
# + ------------------------------------------------- + #

# Import modules / files.
import src.main as launch
import os

try:
    launch._main_root()
except KeyboardInterrupt:
    os.system('cls')
    os.system('exit')
except Exception:
    os.system('cls')
    os.system('exit')
