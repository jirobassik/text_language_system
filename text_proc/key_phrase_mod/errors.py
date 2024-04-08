class KeyPhraseExtractorError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__(errors)

    def __str__(self):
        return self.errors
