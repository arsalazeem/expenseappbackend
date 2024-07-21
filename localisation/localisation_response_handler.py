import os

from enums import HeaderType, Language
from utlis.json_utils import load_json_as_dict


class LocalizedResponseHandler:
    def __init__(self, headers=None):
        self.localised_strings_path = f"{os.getcwd()}/localisation/string.json"
        self.translation_strings = load_json_as_dict(self.localised_strings_path)
        self.Languages = Language
        self.current_locale = None
        try:
            if headers is not None and headers.get(HeaderType.LOCALE.value) is not None:
                if self.is_language_supported():
                    self.current_locale = headers.get(HeaderType.LOCALE.value)
                else:
                    self.current_locale = self.Languages.ENGLISH  # to do to raise an appropriate error here do it in context
            else:
                self.current_locale = self.Languages.ENGLISH
        except Exception as e:
            print(e)
            print("Falling back to english language")
            self.current_locale = self.Languages.ENGLISH

    def is_language_supported(self):
        return self.current_locale in self.Languages

    def getString(self, string_key):
        try:
            msg = self.translation_strings[string_key][self.current_locale.value]
        except KeyError as e:
            raise KeyError(f"{string_key} does not exist in {self.current_locale}") from e
        return msg

    # to use if required in @beforerequest

    def setLocale(self, locale: str):
        self.current_locale = locale

    def getLocale(self):
        return self.current_locale
