#     A simple image previewer app built using Python-Tkinter.
#     Copyright (C) 2021  Kumarjit Das | কুমারজিৎ দাস
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from sys import stderr as sys_stderr
from os.path import expanduser as os_path_expanduser
from os.path import getmtime as os_path_getmtime


class Paths:

    __IMAGEVIEWER_FILE = '.imageviewer'
    __user_path = ''
    __dict_pahts = {
        'settings': [],
        'languages': [],
        'themes': [],
        'numbers': [],
        'alphabets': [],
        'words': []
    }

    def __init__(self):
        """Load the user path and user settings files (*.json).

        Raises:
        ---
        NotADirectoryError and FileNotFoundError
        """
        try:
            self.__user_path = os_path_expanduser('~').replace('\\', '/')
            if len(self.__user_path) == 0:
                raise NotADirectoryError('The user directory could not be '
                                         'found')
            for key in self.__dict_pahts.keys():
                file = f"{self.__user_path}/{self.__IMAGEVIEWER_FILE}/"\
                       f"user-{key}.json"
                time = 0.0
                try:
                    time = os_path_getmtime(file)
                except FileNotFoundError as e:
                    print(f"ERROR: {e}.", file=sys_stderr)
                finally:
                    self.__dict_pahts[key] = [file, time, False]
        except NotADirectoryError as e:
            print(f"ERROR: {e}.", file=sys_stderr)

    def check(self):
        """Checks the user path and user settings files (*.json).

        Raises:
        ---
        NotADirectoryError and FileNotFoundError
        """
        try:
            if len(self.__user_path) == 0:
                self.__user_path = os_path_expanduser('~').replace('\\', '/')
                if len(self.__user_path) == 0:
                    raise NotADirectoryError('The user directory could not be '
                                             'found')
            for value in self.__dict_pahts.values():
                time = value[1]
                try:
                    time = os_path_getmtime(value[0])
                except FileNotFoundError as e:
                    print(f"ERROR: {e}.", file=sys_stderr)
                finally:
                    if time != value[1]:
                        value[1] = time
                        value[2] = True
                    else:
                        value[2] = False
        except NotADirectoryError as e:
            print(f"ERROR: {e}.", file=sys_stderr)

    def is_modified(self, file):
        """Checks if a user settings file (*.json) was modified or not.

        ---
        Parameters:
        ---
        file: str
            -- name of the file (*.json) to be checked

        Raises:
        ---
        KeyError
        """
        modified = False
        try:
            modified = self.__dict_pahts[file][2]
        except KeyError as e:
            print(f'ERROR: {e}.', file=sys_stderr)
        finally:
            return modified

    def __str__(self):
        """Evaluates to the user profile directory"""
        return f'User profile directory: "{self.__user_path}"'


def __Main() -> None:
    """Main entry point of this program"""
    print(
        "ImageViewer::Paths - Contains and handles all the paths.\n"
        "Copyright:\n"
        "    imageviewer::paths  Copyright (C) 2021  Kumarjit Das\n"
        "    This program comes with ABSOLUTELY NO WARRANTY.\n"
        "    This is free software, and you are welcome to redistribute it\n"
        "    under certain conditions."
    )
    # from time import sleep
    # p = Paths()
    # print(p)
    # for _ in range(100):
    #     sleep(3.0)
    #     p.check()
    #     for file in ['settings', 'languages', 'themes',
    #                  'numbers', 'alphabets', 'words']:
    #         if p.is_modified(file):
    #             print(f'*** {file} has been modified.')
    #         else:
    #             print(f'{file} has not been modified.')


if __name__ == "__main__":
    __Main()  # calling the __Main function
