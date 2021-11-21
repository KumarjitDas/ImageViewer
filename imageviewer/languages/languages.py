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
from sys import stderr as sys_stderr


class Languages:

    __PATH_LANGUAGES = 'imageviewer/languages/languages.json'

    __dict_codes = {}
    __dict_names = {}
    __codes = set()
    __names = set()
    __default_code = ''
    __default_name = ''
    __code = ''
    __name = ''

    def __init__(self, path_root, code=''):
        """Load the system languages from the root path.

        ---
        The path_root sould be full path to the root of this project.
        If the code is an empty string the system default language is set. If
        the language corresponding to the code is not in the loaded languages
        list the default language is set as the system default language and a
        ValueError is raised.

        ---
        Parameters:
        ---
        path_root: str
            -- full path to the root of this program

        Keyword arguments:
        ---
        code: str
            -- ISO code of the default language (default ' ')

        Raises:
        ---
        FileNotFoundError and ValueError
        """
        path = path_root + '/' + self.__PATH_LANGUAGES
        with open(file=path, mode='rt', encoding='utf-8') as file:
            dict_languages = json_load(file)
            self.__dict_codes = dict_languages['codes']
            for code_name, display_name in self.__dict_codes.items():
                self.__dict_names[display_name] = code_name
                self.__names.add(display_name)
                self.__codes.add(code_name)
            self.__default_code = dict_languages['default']
            self.__default_name = self.__dict_codes[self.__default_code]
            if len(code) == 0:
                code = self.__default_code
            else:
                try:
                    if code not in self.__codes:
                        raise ValueError(
                            f"'{code}' is not a valid system language code")
                except ValueError as e:
                    print(f"ERROR: {e}.",
                          f"       Valid language codes are: {self.__codes}",
                          f"       Reverting to default language code, "
                          f"'{self.__default_code}'.",
                          sep='\n',
                          file=sys_stderr)
                    code = self.__default_code
            self.__code = code
            self.__name = self.__dict_codes[code]

    def set_code(self, code=''):
        """Set the default language code.

        ---
        If the code is an empty string the system default language is set. If
        the language corresponding to the code is not in the loaded languages
        list the default language is set as the previous default language and a
        ValueError is raised.

        ---
        Keyword arguments:
        ---
        code: str
            -- ISO code of the default language (default ' ')

        Raises:
        ---
        ValueError
        """
        if len(code) == 0:
            self.__code = self.__default_code
            self.__name = self.__default_name
            return
        try:
            if code not in self.__codes:
                raise ValueError(
                    f"'{code}' is not a valid language code")
            else:
                self.__code = code
                self.__name = self.__dict_codes[code]
        except ValueError as e:
            print(f"ERROR: {e}.",
                  f"       Valid language codes are: {self.__codes}",
                  f"       Keeping the default language code, "
                  f"'{self.__code}'.",
                  sep='\n',
                  file=sys_stderr)

    def set_name(self, name=''):
        """Set the default language name.

        ---
        If the name is an empty string the system default language is set. If
        the language corresponding to the name is not in the loaded languages
        list the default language is set as the previous default language and a
        ValueError is raised.

        ---
        Keyword arguments:
        ---
        name: str
            -- display name of the language (default ' ')

        Raises:
        ---
        ValueError
        """
        if len(name) == 0:
            self.__code = self.__default_code
            self.__name = self.__default_name
            return
        try:
            if name not in self.__names:
                raise ValueError(
                    f"'{name}' is not a valid language name")
            else:
                self.__name = name
                self.__code = self.__dict_names[name]
        except ValueError as e:
            print(f"ERROR: {e}.",
                  f"       Valid language names are: {self.__names}",
                  f"       Keeping the default language name, "
                  f"'{self.__name}'.",
                  sep='\n',
                  file=sys_stderr)

    def get_code(self, name=''):
        """Get the language code from the name.

        ---
        If the name is an empty string the previous default code is returned.
        If the code corresponding to the name is not in the loaded languages
        list the previous code is returned and a KeyError is raised.

        ---
        Keyword arguments:
        ---
        name: str
            -- display name of the language (default ' ')

        Returns:
        ---
        : str
            -- ISO code of the language corresponding to the name

        Raises:
        ---
        KeyError
        """
        if len(name) == 0:
            return self.__code
        try:
            return self.__dict_names[name]
        except KeyError as e:
            print(f"ERROR: {e}. '{name}' is not a valid language name.",
                  f"       Valid language names are: {self.__names}",
                  f"       Returning the code for the default language, "
                  f"'{self.__name}'",
                  sep='\n',
                  file=sys_stderr)
            return self.__code

    def get_name(self, code=''):
        """Get the language name from the code.

        ---
        If the code is an empty string the previous default name is returned.
        If the name corresponding to the code is not in the loaded languages
        list the previous name is returned and a KeyError is raised.

        ---
        Keyword arguments:
        ---
        code: str
            -- ISO code of the default language (default ' ')

        Returns:
        ---
        : str
            -- display name of the language corresponding to the code

        Raises:
        ---
        KeyError
        """
        if len(code) == 0:
            return self.__name
        try:
            return self.__dict_codes[code]
        except KeyError as e:
            print(f"ERROR: {e}. '{code}' is not a valid language code.",
                  f"       Valid language codes are: {self.__codes}",
                  f"       Returning the name for the default language code, "
                  f"'{self.__code}'",
                  sep='\n',
                  file=sys_stderr)
            return self.__name

    def get_codes(self):
        """Get the language codes from the languages list.

        Returns:
        ---
        : set[str]
            -- a set of ISO codes of all the languages in the languages list
        """
        return self.__codes

    def get_names(self):
        """Get the language names from the languages list.

        Returns:
        ---
        : set[str]
            -- a set of display names of all the languages in the languages list
        """
        return self.__names

    def load(self, path_full):
        """Load the user languages from the given full path.

        ---
        If the code is an empty string the previous default language is set. If
        the language corresponding to the code is not in the loaded languages
        the default language is set as the previous default language and
        ValueError is raised.

        ---
        Parameters:
        ---
        path_full: str
            -- full path to the user-languages file (*.json)

        Raises:
        ---
        FileNotFoundError and ValueError
        """
        with open(file=path_full, mode='rt', encoding='utf-8') as file:
            dict_languages = json_load(file)
            for code_name, display_name in dict_languages['codes'].items():
                self.__dict_codes[code_name] = display_name
                self.__dict_names[display_name] = code_name
                self.__names.add(display_name)
                self.__codes.add(code_name)
            self.set_code(dict_languages.get('default', self.__code))

    def __str__(self):
        """Evaluates to the default language name and its ISO code"""
        return f"{self.__name} - (ISO:{self.__code})"


def __Main():
    """Main entry point of this program"""
    print(
        "ImageViewer::Languages - Contains and handles all the languages.\n"
        "Copyright:\n"
        "    imageviewer::languages  Copyright (C) 2021  Kumarjit Das\n"
        "    This program comes with ABSOLUTELY NO WARRANTY.\n"
        "    This is free software, and you are welcome to redistribute it\n"
        "    under certain conditions."
    )
    # l = Languages('D:/Repository/ImageViewer')
    # print(f"{l}",
    #       f"{l.get_codes()}",
    #       f"{l.get_names()}",
    #       sep='\n')
    # l.load('D:/Repository/ImageViewer/user-languages.json')
    # print(f"{l}",
    #       f"{l.get_codes()}",
    #       f"{l.get_names()}",
    #       sep='\n')
    # print('--------------------------------')
    # l.set_code()
    # print(l)
    # l.set_code('en-US')
    # print(l)
    # l.set_code('bn-IN')
    # print(l)
    # l.set_code('fu-CK')
    # print(l)
    # print(f"{l.get_code()}",
    #       f"{l.get_name()}",
    #       f"{l.get_code('English (US)')}",
    #       f"{l.get_name('en-US')}",
    #       f"{l.get_code('Bengali (India)')}",
    #       f"{l.get_name('bn-IN')}",
    #       f"{l.get_code('Fuck (World)')}",
    #       f"{l.get_name('fu-CK')}",
    #       f"{l.get_code('Oriya')}",
    #       f"{l.get_name('hn')}",
    #       sep='\n')
    # print('--------------------------------')
    # l.set_name()
    # print(l)
    # l.set_name('English (US)')
    # print(l)
    # l.set_name('Bengali (India)')
    # print(l)
    # l.set_name('Fuck (World)')
    # print(l)
    # print(f"{l.get_code()}",
    #       f"{l.get_name()}",
    #       f"{l.get_code('English (US)')}",
    #       f"{l.get_name('en-US')}",
    #       f"{l.get_code('Bengali (India)')}",
    #       f"{l.get_name('bn-IN')}",
    #       f"{l.get_code('Hindi')}",
    #       f"{l.get_name('or')}",
    #       sep='\n')
    # print('--------------------------------')


if __name__ == "__main__":
    __Main()  # calling the __Main function
