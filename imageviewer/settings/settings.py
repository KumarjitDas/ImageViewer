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

from json import load as json_load
from json import dump as json_dump
from sys import stderr as sys_stderr


class Settings:

    __PATH_SETTINGS = 'imageviewer/settings/settings.json'

    __languages = None
    __strings = None
    __themes = None

    __dict_settings = {}

    __statusbar = None

    def __init__(self, path_root, languages, strings, themes):
        """Load the system settings from the root path.

        ---
        The path_root sould be full path to the root of this project.

        ---
        Parameters:
        ---
        path_root: str
            -- full path to the root of this program

        Raises:
        ---
        FileNotFoundError and ValueError
        """
        path = path_root + '/' + self.__PATH_SETTINGS
        with open(file=path, mode='rt', encoding='utf-8') as file:
            self.__dict_settings = json_load(file)
            code = self.__dict_settings['language']
            languages.set_code(code)
            strings.load_language_codes(languages.get_codes())
            strings.set_language(code)
            themes.set(self.__dict_settings['theme'])
            self.__languages = languages
            self.__strings = strings
            self.__themes = themes
            self.__statusbar = self.__dict_settings['statusbar']

    def set(self, language='', theme='', statusbar=None):
        """Set the default settings.

        ---
        If the name is an empty string the previous default setting is set. If
        the setting corresponding to the name is not in the loaded settings the
        default setting is set as the previous default setting and KeyError is
        raised.

        ---
        Keyword arguments:
        ---
        language: str
            -- ISO language code of the default language (default ' ')
        theme: str
            -- name of the default theme (default ' ')
        statusbar: bool
            -- visibility of the statusbar (default None)

        Raises:
        ---
        KeyError
        """
        self.__languages.set_code(language)
        self.__strings.set_language(language)
        self.__themes.set(theme)
        if statusbar is not None:
            self.__statusbar = statusbar
        self.__dict_settings['language'] = self.__languages.get_code()
        self.__dict_settings['theme'] = self.__themes.get_name()
        self.__dict_settings['statusbar'] = self.__statusbar

    def get(self, thing):
        """Get the setting by name.

        ---
        Parameters:
        ---
        thing: str
            -- name of the thing to return the value of

        Returns:
        ---
        : str | dict | bool
            -- value of the given thing

        Raises:
        ---
        KeyError
        """
        if thing == 'language' or thing == 'language code':
            return self.__languages.get_code()
        if thing == 'language name':
            return self.__languages.get_name()
        if thing == 'theme':
            return self.__themes.get()
        if thing == 'theme_name':
            return self.__themes.get_name()
        if thing == 'statusbar':
            return self.__statusbar
        return None

    def load(self, path_full):
        """Load the user settings from the given full path.

        ---
        The path_full should be full path to the user-settings file in JSON file
        format.

        ---
        Parameters:
        ---
        path_full: str
            -- full path to the user-settings file (*.json)

        Raises:
        ---
        FileNotFoundError and KeyError
        """
        with open(file=path_full, mode='rt', encoding='utf-8') as file:
            dict_settings = json_load(file)
            for name, setting in dict_settings.items():
                self.__dict_settings[name] = setting
            self.set(self.__dict_settings['language'],
                     self.__dict_settings['theme'],
                     self.__dict_settings['statusbar'])

    def dump(self, file):
        """Dump the settings dict into the user-settings file.

        ---
        Parameters:
        ---
        file: TextIOWrapper | FileIO | IO
            -- opened ('wt') file object of the user-settings file (*.json)

        Raises:
        ---
        FileNotFoundError
        """
        try:
            json_dump(self.__dict_settings, file,
                      skipkeys=True,
                      ensure_ascii=False,
                      indent=4)
        except Exception as e:
            print(f"Could not write settings to user-settings file. ",
                  f"ERROR: {e}.",
                  sep='\n',
                  file=sys_stderr)

    def __str__(self):
        """Evaluates to the default settings"""
        return f"{self.__dict_settings}"


def __Main() -> None:
    """Main entry point of this program"""
    print(
        "ImageViewer::Settings - Contains and handles all the settings.\n"
        "Copyright:\n"
        "    imageviewer::settings  Copyright (C) 2021  Kumarjit Das\n"
        "    This program comes with ABSOLUTELY NO WARRANTY.\n"
        "    This is free software, and you are welcome to redistribute it\n"
        "    under certain conditions."
    )
#     from imageviewer.languages.languages import Languages
#     from imageviewer.strings.strings import Strings
#     from imageviewer.themes.themes import Themes
#
#     path_root = 'D:/Repository/ImageViewer'
#     l = Languages(path_root)
#     s = Strings(path_root)
#     t = Themes(path_root)
#     settings = Settings(path_root, l, s, t)
#     print(settings)
#     path_user = 'D:/Repository/ImageViewer/user-settings.json'
#     settings.load(path_user)
#     print(settings)
#     with open(path_user, mode='wt', encoding='utf-8') as file:
#         settings.dump(file)
#     print(f"{settings.get('language')}",
#           f"{settings.get('language code')}",
#           f"{settings.get('language name')}",
#           f"{settings.get('theme')}",
#           f"{settings.get('theme_name')}",
#           f"{settings.get('statusbar')}",
#           sep='\n')
#     print('---------------------------------')
#     settings.set(language='bn-IN')
#     print(f"{settings.get('language')}",
#           f"{settings.get('language code')}",
#           f"{settings.get('language name')}",
#           f"{settings.get('theme')}",
#           f"{settings.get('theme_name')}",
#           f"{settings.get('statusbar')}",
#           sep='\n')
#     print('---------------------------------')
#     settings.set(language='fu-CK')
#     print(f"{settings.get('language')}",
#           f"{settings.get('language code')}",
#           f"{settings.get('language name')}",
#           f"{settings.get('theme')}",
#           f"{settings.get('theme_name')}",
#           f"{settings.get('statusbar')}",
#           sep='\n')
#     print('---------------------------------')
#     settings.set(theme='Dark')
#     print(f"{settings.get('language')}",
#           f"{settings.get('language code')}",
#           f"{settings.get('language name')}",
#           f"{settings.get('theme')}",
#           f"{settings.get('theme_name')}",
#           f"{settings.get('statusbar')}",
#           sep='\n')
#     print('---------------------------------')
#     settings.set(theme='Fuck')
#     print(f"{settings.get('language')}",
#           f"{settings.get('language code')}",
#           f"{settings.get('language name')}",
#           f"{settings.get('theme')}",
#           f"{settings.get('theme_name')}",
#           f"{settings.get('statusbar')}",
#           sep='\n')
#     print('---------------------------------')
#     settings.set(statusbar=False)
#     print(f"{settings.get('language')}",
#           f"{settings.get('language code')}",
#           f"{settings.get('language name')}",
#           f"{settings.get('theme')}",
#           f"{settings.get('theme_name')}",
#           f"{settings.get('statusbar')}",
#           sep='\n')


if __name__ == "__main__":
    __Main()  # calling the __Main function
