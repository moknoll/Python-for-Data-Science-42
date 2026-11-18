from S1E9 import Character


class Baratheon(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self._eyes = "brown"
        self._hairs = "dark"

    @property
    def eyes(self):
        return self._eyes

    @property
    def hairs(self):
        return self._hairs

    @eyes.setter
    def eyes(self, value):
        self._eyes = value

    @hairs.setter
    def hairs(self, value):
        self._hairs = value

    def announce(self):
        print(f"New member of Baratheon: {self.first_name}")

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"


class Lannister(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def announce(self):
        print(f"New member of Lannister: {self.first_name}")

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self._eyes = "blue"
        self._hairs = "light"

    @property
    def eyes(self):
        return self._eyes

    @property
    def hairs(self):
        return self._hairs

    @eyes.setter
    def eyes(self, value):
        self._eyes = value

    @hairs.setter
    def hairs(self, value):
        self._hairs = value

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
