from _2_2speakers_types import Indoors

class VoiceHelper(Indoors):
    languages = ["ru", "en", "de", "esp"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_language(self, lang: str):
        self.languages.append(lang)
        return self.languages