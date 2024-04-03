class MaxLongOperationsError(Exception):
    def __init__(self, errors) -> None:
        self.errors = errors
        super().__init__(errors)
