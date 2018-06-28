import re

class ValidatePassword():

    def match_password_complexity(self, password):
        return [
            any(i.isdigit() for i in password),
            not bool(re.match("^[a-zA-Z0-9_]*$", password)),
            any(x.islower() for x in password),
            any(x.isupper() for x in password)
        ]
    def validate(self):
        print('validated')
