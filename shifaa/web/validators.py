class BaseStringValidator(str):
    def __init__(self, value='', encoding=None, errors='strict', auto_validate=True):
        if auto_validate:
            self.validate(value)
        super(str, BaseStringValidator).__init__(value, encoding=None, errors='strict')

    def validate(self, value):
        raise ValueError('Not know value')


class EmailValidator(BaseStringValidator):
    def validate(self, value):
        # Check that the value match a certain choices
        # Do all the necessary information about the email here :)
        pass
