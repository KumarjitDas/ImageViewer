import json


class Strings:

    __path_numbers = "imageviewer/strings/numbers.json"
    __path_alphabets = "imageviewer/strings/alphabets.json"
    __path_words = "imageviewer/strings/words.json"

    __DEFAULT_LANGUAGE_CODE = 'en-US'
    __language_code = __DEFAULT_LANGUAGE_CODE

    __dict_numbers = {}
    __dict_alphabets = {}
    __dict_words = {}

    __list_numbers = []
    __list_alphabets = []

    def __set_paths(self, path_root):
        self.__path_numbers = path_root + '/' + self.__path_numbers
        self.__path_alphabets = path_root + '/' + self.__path_alphabets
        self.__path_words = path_root + '/' + self.__path_words

    def __set_list_numbers(self, language_code=''):
        if len(language_code) == 0:
            language_code = self.__language_code
        elif language_code == self.__language_code:
            return
        self.__list_numbers = self.__dict_numbers.get(language_code, [])

    def __set_list_alphabets(self, language_code=''):
        if len(language_code) == 0:
            language_code = self.__language_code
        elif language_code == self.__language_code:
            return
        self.__list_alphabets = self.__dict_alphabets.get(language_code, [])

    def __init__(self, path_root, language_code=''):
        self.__set_paths(path_root)
        if len(language_code) == 0:
            language_code = self.__DEFAULT_LANGUAGE_CODE
        with open(file=self.__path_numbers,
                  mode='rt',
                  encoding='utf-8') as file:
            self.__dict_numbers = json.load(file)
            self.__set_list_numbers(language_code)
        with open(file=self.__path_alphabets,
                  mode='rt',
                  encoding='utf-8') as file:
            self.__dict_alphabets = json.load(file)
            self.__set_list_alphabets(language_code)
        with open(file=self.__path_words,
                  mode='rt',
                  encoding='utf-8') as file:
            self.__dict_words = json.load(file)
        self.__language_code = language_code

    def set_language(self, code):
        if len(code) == 0:
            return
        self.__set_list_numbers(code)
        self.__set_list_alphabets(code)
        self.__language_code = code

    def get_number(self, number, language_code=''):
        string = str(number)
        if len(language_code) == 0:
            language_code = self.__language_code
        if language_code == self.__DEFAULT_LANGUAGE_CODE:
            return string
        numbers = self.__list_numbers
        if len(numbers) == 0:
            numbers = self.__dict_numbers.get(language_code, [])
            if len(numbers) == 0:
                return string
        return string.replace('0', numbers[0]).replace('1', numbers[1])\
                     .replace('2', numbers[2]).replace('3', numbers[3])\
                     .replace('4', numbers[4]).replace('5', numbers[5])\
                     .replace('6', numbers[6]).replace('7', numbers[7])\
                     .replace('8', numbers[8]).replace('9', numbers[9])

    def get_abbreviation(self, string, language_code=''):
        string = string.upper()
        if len(language_code) == 0:
            language_code = self.__language_code
        if language_code == self.__DEFAULT_LANGUAGE_CODE:
            return string
        alphabets = self.__list_alphabets
        if len(alphabets) == 0:
            alphabets = self.__dict_alphabets.get(language_code, [])
            if len(alphabets) == 0:
                return string
        string = self.get_number(string, language_code)
        return string.replace('A', alphabets[0]).replace('B', alphabets[1])\
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
        if len(language_code) == 0:
            language_code = self.__language_code
        if language_code == self.__DEFAULT_LANGUAGE_CODE:
            return string
        value = self.__dict_words.get(string, string)
        if type(value) is str:
            return value
        return value.get(language_code, string)


def main():
    """Main entry point of this program"""
    print("ImageViewer::Strings - Contains and handles all the strings\n"
          "                       and their translations.")


if __name__ == "__main__":
    main()  # calling the main function
