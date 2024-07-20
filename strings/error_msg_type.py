from enums.language import Language

class LocalizedResponseHandler:
    def __init__(self, headers=None):
        self.translation_strings = msgs
        self.Languages = Language
        if headers is None or headers.get("locale") is None:
            self.current_locale = self.Languages.ENGLISH
        else:
            self.current_locale = headers.get("locale")
    
    def is_language_supported(self):
        return self.current_locale in self.Languages

    def getString(self, string_key):
        try:
            msg = self.translation_strings[string_key][self.current_locale]
        except KeyError as e:
            raise KeyError(f"{string_key} does not exist in {self.current_locale}") from e
        return msg

 







