class ValidUserName:
    def __init__(self):
        pass

    def __set_name__(self, owner_class, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.name} must be a string')
        if len(value) == 0:
            raise ValueError(f'Should contain atleast one charecter')
        self.name = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self.name      

class ValidEmailId:
    def __init__(self):
        pass

    def __set_name__(self, owner_class, name):
        self.mailid = name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.mailid} must contain a @ and .')
        if len(value) == 0:
            raise ValueError(f'Should contain atleast one charecter')
        if '.' in value and '@' in value:
            self.mailid = value
        else:
            self.mailid = None
            raise ValueError("Cannot create valid E-Mail ID")

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self.mailid

class UserProfileManager:
    last_login = None
    username = ValidUserName()
    email = ValidEmailId()