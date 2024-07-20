msgs = {
    "1": {
        "en": "User with this email already exists"
    }
}

from enums.language import Language

class ResponseString:
    def __init__(self,headers=None):
        self.translation_strings=msgs
        if headers is None or headers.get("locale") is None:
            self.current_locale = Language.ENGLISH
        else:
            self.current_locale=headers.



    @staticmethod
    def is_language_supported():






    def get_response_string(self):

