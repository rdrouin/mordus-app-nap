class User:
    def __init__(self, username, hashedPassword):
        self.id = username
        self.hashedPassword = hashedPassword
        self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = False

    def get_id(self):
        return self.id

    def __eq__(self, other):
        if isinstance(other, User):
            return self.id == other.id and self.hashedPassword == other.hashedPassword
        if isinstance(other, str):
            return self.id == other
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
