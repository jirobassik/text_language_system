class MaxLongOperationsError(Exception):
    def __init__(self, errors) -> None:
        self.errors = [
            {
                "type": "max_long_operations_error",
                "msg": "Other long task must be completed",
            }
        ]
        super().__init__(errors)
