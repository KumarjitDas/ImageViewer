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
import sys


class Themes:

    __PATH_THEMES = 'imageviewer/themes/themes.json'

    __dict_themes = {}
    __names = set()
    __theme = {}
    __default_name = ''
    __name = ''

    def load(self, path_full, name=''):
        """Load the user themes from the given full path.

        ---
        If the name is an empty string the previous default theme is set. If
        the theme corresponding to the name is not in the loaded themes the
        default theme is set as the previous default theme and KeyError is
        raised.

        ---
        Parameters:
        ---
        path_full: str
            -- full path to the user-themes file (*.json)

        Keyword arguments:
        ---
        name: str
            -- name of the default theme (default ' ')

        Raises:
        ---
        KeyError
        """
        with open(file=path_full, mode='rt', encoding='utf-8') as file:
            dict_themes = json.load(file)
        for theme_name, theme in dict_themes.items():
            if isinstance(theme, dict):
                self.__dict_themes[theme_name] = theme
                self.__names.add(theme_name)
        self.__default_name = dict_themes.get('default', self.__default_name)
        name = dict_themes.get('default', name)
        self.set_default(name)

    def __init__(self, path_root, name=''):
        """Load the system themes from the root path.

        ---
        If the name is an empty string the default theme, 'Light' is set. If
        the theme corresponding to the name is not in the loaded themes the
        default theme is set as 'Light' and KeyError is raised.

        ---
        Parameters:
        ---
        path_root: str
            -- full path to the root of this program

        Keyword arguments:
        ---
        name: str
            -- name of the default theme (default ' ')

        Raises:
        ---
        KeyError
        """
        path = path_root + '/' + self.__PATH_THEMES
        with open(file=path, mode='rt', encoding='utf-8') as file:
            dict_themes = json.load(file)
        for theme_name, theme in dict_themes.items():
            if isinstance(theme, dict):
                self.__dict_themes[theme_name] = theme
                self.__names.add(theme_name)
        self.__default_name = dict_themes['default']
        if len(name) == 0:
            name = self.__default_name
        try:
            if name not in self.__names:
                raise Exception(f"'{name}' is not a valid system theme")
        except Exception as e:
            print(f"ERROR: {e}.",
                  f"       Valid themes are: {self.__names}",
                  f"       Reverting to default theme, "
                      f"'{self.__default_name}'.",
                  sep='\n',
                  file=sys.stderr)
            name = self.__default_name
        self.__name = name
        self.__theme = self.__dict_themes[name]

    def set_default(self, name=''):
        """Set the default theme.

        ---
        If the name is an empty string the previous default theme is set. If
        the theme corresponding to the name is not in the loaded themes the
        default theme is set as the previous default theme and KeyError is
        raised.

        ---
        Keyword arguments:
        ---
        name: str
            -- name of the default theme (default ' ')

        Raises:
        ---
        KeyError
        """
        if len(name) == 0:
            name = self.__default_name
        if name == self.__name:
            return
        theme = {}
        try:
            theme = self.__dict_themes[name]
        except KeyError as e:
            print(f"ERROR: {e}. '{name}' is not a valid theme.",
                  f"       Valid themes are: {self.__names}",
                  f"       Reverting to default theme, '{self.__name}'.",
                  sep='\n',
                  file=sys.stderr)
            return
        self.__name = name
        self.__theme = theme

    def get(self, name=''):
        """Get the theme by name.

        ---
        If the name is an empty string the default theme is returned. If the
        the theme corresponding to the name is not in the loaded themes the
        default theme is returned and KeyError is raised.

        ---
        Keyword arguments:
        ---
        name: str
            -- name of the default theme (default ' ')

        Returns:
        ---
        : dict
            -- a dict containing the theme

        Raises:
        ---
        KeyError
        """
        if len(name) == 0:
            return self.__theme
        theme = {}
        try:
            theme = self.__dict_themes[name]
        except KeyError as e:
            print(f"ERROR: {e}. '{name}' is not a valid theme.",
                  f"       Valid themes are: {self.__names}",
                  f"       Returning the default theme, '{self.__name}'.",
                  sep='\n',
                  file=sys.stderr)
            theme = self.__theme
        return theme

    def get_names(self):
        """Get the list of theme names.

        ---
        Returns:
        ---
        : set
            -- a set containing all the theme names
        """
        return self.__names

    def __str__(self):
        """Evaluates to the default theme name"""
        return self.__name


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
    # t = Themes('D:/Repository/ImageViewer', 'Spark')
    # print(
    #     f"{t}",
    #     f"{t.get_names()}",
    #     f"{t.get()}",
    #     f"{t.get('Light')}",
    #     f"{t.get('Dark')}",
    #     f"{t.get('Monokai')}",
    #     sep='\n------------------------------\n'
    # )
    # t.set_default()
    # print(t)
    # t.set_default('Light')
    # print(t)
    # t.set_default('Dark')
    # print(t)
    # t.set_default('Monokai')
    # print(t)
    # print('------------------------------')
    # t.load('D:/Repository/ImageViewer/user-themes.json')
    # print(
    #     f"{t}",
    #     f"{t.get_names()}",
    #     f"{t.get()}",
    #     f"{t.get('Light')}",
    #     f"{t.get('Dark')}",
    #     f"{t.get('AE')}",
    #     f"{t.get('BF')}",
    #     f"{t.get('Monokai')}",
    #     sep='\n------------------------------\n'
    # )
    # t.set_default()
    # print(t)
    # t.set_default('Light')
    # print(t)
    # t.set_default('Dark')
    # print(t)
    # t.set_default('AE')
    # print(t)
    # t.set_default('BF')
    # print(t)
    # t.set_default('Monokai')
    # print(t)


if __name__ == "__main__":
    main()
