import re

class ValidatePassword():
    # def __init__(self):
        # self.exception_messages = 'dfg'

    def validate(self, password):
        validation_schema = [
            self.has_complexity(password),
            self.has_enough_characters(password),
            self.has_not_reached_character_limit(password),
            self.has_no_spaces(password)
        ]
        if False in validation_schema:
            return False
        else:
            return True


    def has_complexity(self, password):
        if self._match_password_complexity(password).count(True) < 3:
            self._exception_messages = 'You must have three of the following four requirements: a special character an uppercase character,a lowercase character or a numerical digit.'
            return False
        else:
            return True

    def has_enough_characters(self, password):
        if len(password) < 8:
            self._exception_messages = 'Your password must be 8 characters or longer.'
            return False
        else:
            return True

    def has_not_reached_character_limit(self, password):
        if len(password) > 20:
            self._exception_messages= 'Your password must be shorter than 20 characters'
            return False
        else:
            return True

    def has_no_spaces(self, password):
        if " " in password:
            self._exception_messages.set = 'Your password cannot contain a space.'
            return False
        else:
            return True

    def _match_password_complexity(self, password):
        return [
            any(i.isdigit() for i in password),
            not bool(re.match("^[a-zA-Z0-9_]*$", password)),
            any(x.islower() for x in password),
            any(x.isupper() for x in password)
        ]

    @property
    def exception_messages(self):
        print('heefds')
        return self._exception_messages

    @exception_messages.setter
    def exception_messages(self, message):
        print('hello world')
        self._exception_messages = message
