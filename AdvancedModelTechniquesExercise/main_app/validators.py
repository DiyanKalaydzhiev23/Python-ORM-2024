from django.core.exceptions import ValidationError


def validate_name(value):
    for char in value:
        if not (char.isalpha() or char.isspace()):
            raise ValidationError("Name can only contain letters and spaces")


class ValidateName:
    def __init__(self, message: str):
        self.message = message

    def __call__(self, value):
        for char in value:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.ValidateName',
            (self.message, ),
            {}
        )
