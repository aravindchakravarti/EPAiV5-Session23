import weakref

class ValidUserName:
    def __set_name__(self, owner_class, name):
        # Automatically called to set the name of the descriptor attribute in the owner class
        self.private_name = f"_{name}"

    def __set__(self, instance, value):
        # Validates and sets the username for the instance
        if not isinstance(value, str):
            raise ValueError('Username must be a string.')
        if not value.strip():
            raise ValueError('Username should contain at least one character.')
        setattr(instance, self.private_name, value)

    def __get__(self, instance, owner_class):
        # Retrieves the username value or the descriptor itself if called from the class
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

class ValidEmailId:
    def __set_name__(self, owner_class, name):
        # Automatically called to set the name of the descriptor attribute in the owner class
        self.private_name = f"_{name}"

    def __set__(self, instance, value):
        # Validates and sets the email for the instance
        if not isinstance(value, str):
            raise ValueError('Email must be a string.')
        if len(value) == 0:
            raise ValueError('Email should contain at least one character.')
        if '.' in value and '@' in value:
            setattr(instance, self.private_name, value)
        else:
            raise ValueError('Invalid email format.')

    def __get__(self, instance, owner_class):
        # Retrieves the email value or the descriptor itself if called from the class
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

class UserProfileManager:
    # Manages user profiles with caching using weak references
    # Tracks the last login time (not implemented here)
    last_login = None  

     # Descriptor for username validation
    username = ValidUserName() 

    # Descriptor for email validation
    email = ValidEmailId()  

    # Cache for managing weak references to user profiles
    values = weakref.WeakValueDictionary()  
    
    @classmethod
    def add_to_cache(cls, object_addr):
        # Adds a user profile object to the weak reference cache
        cls.values[id(object_addr)] = object_addr

    @classmethod
    def get_from_cache(cls, object_addr):
        # Retrieves a user profile object from the weak reference cache
        return cls.values.get(object_addr)
