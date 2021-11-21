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


class Strings:

    __PATH_NUMBERS = "imageviewer/strings/numbers.json"
    __PATH_ALPHABETS = "imageviewer/strings/alphabets.json"
    __PATH_WORDS = "imageviewer/strings/words.json"
    __DEFAULT_LANGUAGE_CODE = 'en-US'

    __language_code = ''
    __language_codes = set((__DEFAULT_LANGUAGE_CODE,))

    __dict_numbers = {}
    __dict_alphabets = {}
    __dict_words = {}

    __list_numbers = []
    __list_alphabets = []

    def __init__(self, path_root, language_code=''):
        """Load the system strings from the root path.

        ---
        The path_root sould be full path to the root of this project.
        If the language_code is an empty string 'en-US' is set as the default
        language. If the language corresponding to the language_code is not in
        the loaded languages list 'en-US' is set as the default language and a
        ValueError is raised.

        ---
        Parameters:
        ---
        path_root: str
            -- full path to the root of this program

        Keyword arguments:
        ---
        language_code: str
            -- ISO language code of the default language (default ' ')

        Raises:
        ---
        FileNotFoundError and ValueError
        """
        self.__language_code = self.__DEFAULT_LANGUAGE_CODE
        if len(language_code) > 0:
            try:
                if language_code not in self.__language_codes:
                    raise ValueError(f"'{language_code}' is not a valid "
                                     "language code")
                else:
                    self.__language_code = language_code
            except ValueError as e:
                print(f"ERROR: {e}.",
                      f"       Valid language codes are: "
                      f"{self.__language_codes}",
                      f"       Reverting to default language code, "
                      f"'{self.__language_code}'.",
                      sep='\n',
                      file=sys_stderr)
                self.__language_code = self.__DEFAULT_LANGUAGE_CODE
        path = path_root + '/' + self.__PATH_NUMBERS
        with open(file=path, mode='rt', encoding='utf-8') as file:
            self.__dict_numbers = json_load(file)
            self.__list_numbers = self.__dict_numbers.get(self.__language_code,
                                                          [])
        path = path_root + '/' + self.__PATH_ALPHABETS
        with open(file=path, mode='rt', encoding='utf-8') as file:
            self.__dict_alphabets = json_load(file)
            self.__list_alphabets = self.__dict_alphabets.get(
                self.__language_code, [])
        path = path_root + '/' + self.__PATH_WORDS
        with open(file=path, mode='rt', encoding='utf-8') as file:
            self.__dict_words = json_load(file)

    def load_language_codes(self, language_codes):
        """Set the set of supported ISO language codes.

        ---
        Parameters:
        ---
        language_codes: set
            -- a set of all supported ISO language codes
        """
        for code in language_codes:
            self.__language_codes.add(code)

    def set_language(self, language_code=''):
        """Set the set of supported ISO language codes.

        ---
        Keyword arguments:
        ---
        language_code: str
            -- ISO language code of the default language (default ' ')
        """
        if len(language_code) == 0:
            self.__language_code = self.__DEFAULT_LANGUAGE_CODE
        else:
            try:
                if language_code not in self.__language_codes:
                    raise ValueError(f"'{language_code}' is not a valid "
                                     "language code")
                else:
                    self.__language_code = language_code
            except ValueError as e:
                print(f"ERROR: {e}.",
                      f"       Valid language codes are: "
                      f"{self.__language_codes}",
                      f"       Keeping the previous default language code, "
                      f"'{self.__language_code}'.",
                      sep='\n',
                      file=sys_stderr)
        self.__list_numbers = self.__dict_numbers.get(self.__language_code, [])
        self.__list_alphabets = self.__dict_alphabets.get(self.__language_code,
                                                          [])

    def get_language(self):
        """Returns the default ISO language code"""
        return self.__language_code

    def get_number(self, number, language_code=''):
        """Get the number as a string in the provided language.

        ---
        Parameters:
        ---
        number: int | float
            -- an integer or floating point value

        Keyword arguments:
        ---
        language_code: str
            -- ISO language code of the default language (default ' ')

        Returns:
        ---
        : str
            -- a stringified number
        """
        string = str(number)
        if len(language_code) == 0:
            language_code = self.__language_code
        if language_code is self.__DEFAULT_LANGUAGE_CODE:
            return string
        numbers = self.__dict_numbers.get(language_code, self.__list_numbers)
        if len(numbers) == 0:
            return string
        return string.replace('0', numbers[0]).replace('1', numbers[1])\
                     .replace('2', numbers[2]).replace('3', numbers[3])\
                     .replace('4', numbers[4]).replace('5', numbers[5])\
                     .replace('6', numbers[6]).replace('7', numbers[7])\
                     .replace('8', numbers[8]).replace('9', numbers[9])

    def get_abbreviation(self, string, language_code=''):
        """Get the abbreviation of the string in the provided language.

        ---
        Parameters:
        ---
        string: str
            -- a string to be abbreviated

        Keyword arguments:
        ---
        language_code: str
            -- ISO language code of the default language (default ' ')

        Returns:
        ---
        : str
            -- an abbreviated string
        """
        if len(string) == 0:
            return ''
        string = string.upper()
        if len(language_code) == 0:
            language_code = self.__language_code
        if language_code is self.__DEFAULT_LANGUAGE_CODE:
            return string
        alphabets = self.__dict_alphabets.get(language_code,
                                              self.__list_alphabets)
        if len(alphabets) == 0:
            return string
        return self.get_number(string, language_code)\
            .replace('A', alphabets[0]).replace('B', alphabets[1])\
            .replace('C', alphabets[2]).replace('D', alphabets[3])\
            .replace('E', alphabets[4]).replace('F', alphabets[5])\
            .replace('G', alphabets[6]).replace('H', alphabets[7])\
            .replace('I', alphabets[8]).replace('J', alphabets[9])\
            .replace('K', alphabets[10]).replace('L', alphabets[11])\
            .replace('M', alphabets[12]).replace('N', alphabets[13])\
            .replace('O', alphabets[14]).replace('P', alphabets[15])\
            .replace('Q', alphabets[16]).replace('R', alphabets[17])\
            .replace('S', alphabets[18]).replace('T', alphabets[19])\
            .replace('U', alphabets[20]).replace('V', alphabets[21])\
            .replace('W', alphabets[22]).replace('X', alphabets[23])\
            .replace('Y', alphabets[24]).replace('Z', alphabets[25])

    def get_word(self, string, language_code=''):
        """Get the string translated in the provided language.

        ---
        Parameters:
        ---
        string: str
            -- a string to be translated

        Keyword arguments:
        ---
        language_code: str
            -- ISO language code of the default language (default ' ')

        Returns:
        ---
        : str
            -- an translated string
        """
        if len(language_code) == 0 or \
           language_code not in self.__language_codes:
            language_code = self.__language_code
        if language_code is self.__DEFAULT_LANGUAGE_CODE:
            return string
        value = self.__dict_words.get(string, string)
        if isinstance(value, str):
            return value
        return value.get(language_code, string)

    def load_numbers(self, path_full):
        """Load the user defined numbers from the given full path.

        ---
        The path_full should be full path to the user-numbers file in JSON file
        format.

        ---
        Parameters:
        ---
        path_full: str
            -- full path to the user-numbers file (*.json)

        Raises:
        ---
        FileNotFoundError and ValueError
        """
        with open(file=path_full, mode='rt', encoding='utf-8') as file:
            dict_numbers = json_load(file)
            for code, numbers in dict_numbers.items():
                self.__dict_numbers[code] = numbers

    def load_alphabets(self, path_full):
        """Load the user defined strings from the given full path.

        ---
        The path_full should be full path to the user-alphabets file in JSON
        file format.

        ---
        Parameters:
        ---
        path_full: str
            -- full path to the user-alphabets file (*.json)

        Raises:
        ---
        FileNotFoundError and ValueError
        """
        with open(file=path_full, mode='rt', encoding='utf-8') as file:
            dict_alphabets = json_load(file)
            for code, alphabets in dict_alphabets.items():
                self.__dict_alphabets[code] = alphabets

    def load_words(self, path_full):
        """Load the user defined strings from the given full path.

        ---
        The path_full should be full path to the user-words file in JSON file
        format.

        ---
        Parameters:
        ---
        path_full: str
            -- full path to the user-words file (*.json)

        Raises:
        ---
        FileNotFoundError and ValueError
        """
        with open(file=path_full, mode='rt', encoding='utf-8') as file:
            dict_words = json_load(file)
            for word, codes in dict_words.items():
                _codes = self.__dict_words.get(word, {})
                if len(_codes) == 0:
                    self.__dict_words[word] = codes
                else:
                    for code, translation in codes.items():
                        _codes[code] = translation

    def __str__(self):
        """Evaluates to number of languages, words, and default ISO language
           code
        """
        return f"{len(self.__language_codes)} language(s), "\
               f"{len(self.__dict_words)} word(s), "\
               f"ISO:{self.__language_code}"


def __Main():
    """Main entry point of this program"""
    print(
        "ImageViewer::Strings - Contains and handles all the strings\n"
        "                     and their translations.\n"
        "Copyright:\n"
        "    imageviewer::strings  Copyright (C) 2021  Kumarjit Das\n"
        "    This program comes with ABSOLUTELY NO WARRANTY.\n"
        "    This is free software, and you are welcome to redistribute it\n"
        "    under certain conditions."
    )
    s = Strings('D:/Repository/ImageViewer', 'bn-IN')
    print(s)
    s.load_language_codes(('bn-IN', 'hn'))
    # print(s)
    # s.set_language('en-US')
    # print(s.get_language())
    # s.set_language('bn-IN')
    # print(s.get_language())
    # print('------------------------------------')
    # s.set_language()
    # print(f"{s.get_number(1234)}",
    #       f"{s.get_number(69, 'en-US')}",
    #       f"{s.get_number(420, 'bn-IN')}",
    #       f"{s.get_number(42069, 'fu-CK')}",
    #       sep='\n')
    # print('------------------------------------')
    # s.set_language('bn-IN')
    # print(f"{s.get_number(1234)}",
    #       f"{s.get_number(420, 'bn-IN')}",
    #       f"{s.get_number(42069, 'fu-CK')}",
    #       f"{s.get_number(69, 'en-US')}",
    #       sep='\n')
    # print('------------------------------------')
    # print(f"{s.get_abbreviation('abc')}",
    #       f"{s.get_abbreviation('a1b2c3')}",
    #       f"{s.get_abbreviation('abc', 'bn-IN')}",
    #       f"{s.get_abbreviation('a1b2c3', 'bn-IN')}",
    #       f"{s.get_abbreviation('abc', 'fu-CK')}",
    #       f"{s.get_abbreviation('a1b2c3', 'fu-CK')}",
    #       f"{s.get_abbreviation('abc', 'en-US')}",
    #       f"{s.get_abbreviation('a1b2c3', 'en-US')}",
    #       sep='\n')
    # print('------------------------------------')
    # s.load_language_codes(('bn-IN',))
    # s.set_language('bn-IN')
    # print(f"{s.get_abbreviation('abc')}",
    #       f"{s.get_abbreviation('a1b2c3')}",
    #       f"{s.get_abbreviation('abc', 'en-US')}",
    #       f"{s.get_abbreviation('a1b2c3', 'en-US')}",
    #       f"{s.get_abbreviation('abc', 'fu-CK')}",
    #       f"{s.get_abbreviation('a1b2c3', 'fu-CK')}",
    #       f"{s.get_abbreviation('abc', 'bn-IN')}",
    #       f"{s.get_abbreviation('a1b2c3', 'bn-IN')}",
    #       sep='\n')
    # print('------------------------------------')
    # print(f"{s.get_word('ImageViewer')}",
    #       f"{s.get_word('Light')}",
    #       f"{s.get_word('Abcdef')}",
    #       f"{s.get_word('ImageViewer', 'bn-IN')}",
    #       f"{s.get_word('Light', 'bn-IN')}",
    #       f"{s.get_word('Abcdef', 'bn-IN')}",
    #       f"{s.get_word('ImageViewer', 'en-US')}",
    #       f"{s.get_word('Light', 'en-US')}",
    #       f"{s.get_word('Abcdef', 'en-US')}",
    #       f"{s.get_word('ImageViewer', 'fu-CK')}",
    #       f"{s.get_word('Light', 'fu-CK')}",
    #       f"{s.get_word('Abcdef', 'fu-CK')}",
    #       sep='\n')
    # print('------------------------------------')
    # s.load_language_codes(('bn-IN',))
    # s.set_language('bn-IN')
    # print(f"{s.get_word('ImageViewer')}",
    #       f"{s.get_word('Light')}",
    #       f"{s.get_word('Abcdef')}",
    #       f"{s.get_word('ImageViewer', 'en-US')}",
    #       f"{s.get_word('Light', 'en-US')}",
    #       f"{s.get_word('Abcdef', 'en-US')}",
    #       f"{s.get_word('ImageViewer', 'bn-IN')}",
    #       f"{s.get_word('Light', 'bn-IN')}",
    #       f"{s.get_word('Abcdef', 'bn-IN')}",
    #       f"{s.get_word('ImageViewer', 'fu-CK')}",
    #       f"{s.get_word('Light', 'fu-CK')}",
    #       f"{s.get_word('Abcdef', 'fu-CK')}",
    #       sep='\n')
    # print('------------------------------------')
    # s.load_numbers('D:/Repository/ImageViewer/user-numbers.json')
    # s.set_language()
    # print(f"{s.get_number(1234)}",
    #       f"{s.get_number(69, 'en-US')}",
    #       f"{s.get_number(420, 'bn-IN')}",
    #       f"{s.get_number(42069, 'hn')}",
    #       f"{s.get_number(42069, 'fu-CK')}",
    #       sep='\n')
    # print('------------------------------------')
    # s.set_language('bn-IN')
    # print(f"{s.get_number(1234)}",
    #       f"{s.get_number(69, 'en-US')}",
    #       f"{s.get_number(420, 'bn-IN')}",
    #       f"{s.get_number(42069, 'hn')}",
    #       f"{s.get_number(42069, 'fu-CK')}",
    #       sep='\n')
    # print('------------------------------------')
    # s.set_language('hn')
    # print(f"{s.get_number(1234)}",
    #       f"{s.get_number(69, 'en-US')}",
    #       f"{s.get_number(420, 'bn-IN')}",
    #       f"{s.get_number(42069, 'hn')}",
    #       f"{s.get_number(42069, 'fu-CK')}",
    #       sep='\n')
    # print('------------------------------------')
    # s.load_words('D:/Repository/ImageViewer/user-words.json')
    # print(f"{s.get_word('ImageViewer')}",
    #       f"{s.get_word('Light')}",
    #       f"{s.get_word('Abcdef')}",
    #       f"{s.get_word('ImageViewer', 'bn-IN')}",
    #       f"{s.get_word('Light', 'bn-IN')}",
    #       f"{s.get_word('Abcdef', 'bn-IN')}",
    #       f"{s.get_word('ImageViewer', 'en-US')}",
    #       f"{s.get_word('Light', 'en-US')}",
    #       f"{s.get_word('Abcdef', 'en-US')}",
    #       f"{s.get_word('ImageViewer', 'hn')}",
    #       f"{s.get_word('Light', 'hn')}",
    #       f"{s.get_word('Abcdef', 'hn')}",
    #       f"{s.get_word('ImageViewer', 'fu-CK')}",
    #       f"{s.get_word('Light', 'fu-CK')}",
    #       f"{s.get_word('Abcdef', 'fu-CK')}",
    #       sep='\n')
    # print('------------------------------------')
    # s.set_language('hn')
    # print(f"{s.get_word('ImageViewer')}",
    #       f"{s.get_word('Light')}",
    #       f"{s.get_word('Abcdef')}",
    #       f"{s.get_word('ImageViewer', 'en-US')}",
    #       f"{s.get_word('Light', 'en-US')}",
    #       f"{s.get_word('Abcdef', 'en-US')}",
    #       f"{s.get_word('ImageViewer', 'bn-IN')}",
    #       f"{s.get_word('Light', 'bn-IN')}",
    #       f"{s.get_word('Abcdef', 'bn-IN')}",
    #       f"{s.get_word('ImageViewer', 'hn')}",
    #       f"{s.get_word('Light', 'hn')}",
    #       f"{s.get_word('Abcdef', 'hn')}",
    #       f"{s.get_word('ImageViewer', 'fu-CK')}",
    #       f"{s.get_word('Light', 'fu-CK')}",
    #       f"{s.get_word('Abcdef', 'fu-CK')}",
    #       sep='\n')


if __name__ == "__main__":
    __Main()  # calling the __Main function
