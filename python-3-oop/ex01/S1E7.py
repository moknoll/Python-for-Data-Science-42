from S1E9 import Character


class Baratheon(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def announce(self):
        print(f"New member of Baratheon: {self.first_name}")

    def __str__(self):
        return f"Vector: ({self.first_name}, {self.family_name}, {self.eyes} \
                        , {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.first_name}, {self.family_name}, {self.eyes} \
                        , {self.hairs})"


class Lannister(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def announce(self):
        print(f"New member of Lannister: {self.first_name}")

    def __str__(self):
        return f"Vector: ({self.first_name}, {self.family_name}, {self.eyes} \
                        , {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.first_name}, {self.family_name}, {self.eyes} \
                        , {self.hairs})"

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
