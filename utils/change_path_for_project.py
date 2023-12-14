import os


"""
The 'os' library enables file and directory manipulation, as well as
system command execution.

It's utilized to ensure relative pathing, preventing conflicts when
executing code from locations not recognized by Python by default.
This library provides functionalities to work with files, directories,
and execute system commands.
"""


def change_path():
    # Gets the path to the current script
    script_dir = os.path.dirname(__file__)
    # Changes the current working directory to the script directory
    os.chdir(script_dir)