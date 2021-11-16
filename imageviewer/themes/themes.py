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

import json


class Themes:

    __PATH_THEMES = 'imageviewer/themes/themes.json'
    __DEFAULT_NAME = 'Light'

    __dict_themes = {}
    __theme = None
    __names = set()
    __name = ''

    def load(self, path_full, name=''):
        """Load the system themes from the given full path.

        Parameters:
        ---
        path_full: str
            -- full path to the '*themes.json' file

        Keyword arguments:
        ---
        name: str
            -- name of the default theme (default 'Light')
        """
        with open(file=path_full, mode='rt', encoding='utf-8') as file:
            dict_themes = json.load(file)
        for theme_name in dict_themes.keys():
            self.__dict_themes[theme_name] = dict_themes[theme_name]
            self.__names.add(theme_name)
        self.__name = self.__DEFAULT_NAME
        self.__theme = self.__dict_themes[self.__name]
        self.set_default(name)

    def __init__(self, path_root, name=''):
        """Load the system themes from the root path.

        Parameters:
        ---
        path_root: str
            -- full path to the root of this program

        Keyword arguments:
        ---
        name: str
            -- name of the default theme (default 'Light')
        """
        path = path_root + '/' + self.__PATH_THEMES
        self.load(path, name)

    def set_default(self, name=''):
        """Set the default theme.

        Keyword arguments:
        ---
        name: str
            -- name of the default theme (default 'Light')
        """
        if len(name) == 0:
            name = self.__DEFAULT_NAME
        if name == self.__name:
            return
        theme = self.__dict_themes.get(name, self.__theme)
        if theme is not self.__theme:
            self.__name = name
            self.__theme = theme

    def get(self, name=''):
        """Get the theme by name.

        Keyword arguments:
        ---
        name: str
            -- name of the default theme (default 'Light')

        Returns:
        ---
        : dict
            -- a dict containing the theme
        """
        return self.__dict_themes.get(name, self.__theme)

    def get_names(self):
        """Get the list of theme names.

        Returns:
        ---
        : list
            -- a list containing all the themes
        """
        return list(self.__names)


def main():
    """Main entry point of this program"""
    print(
        "ImageViewer::Themes - Contains and handles all the themes.\n"
        "Copyright:\n"
        "    imageviewer::themes  Copyright (C) 2021  Kumarjit Das\n"
        "    This program comes with ABSOLUTELY NO WARRANTY.\n"
        "    This is free software, and you are welcome to redistribute it\n"
        "    under certain conditions."
    )


if __name__ == "__main__":
    main()
