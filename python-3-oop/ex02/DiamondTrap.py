from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class inheriting from Baratheon and Lannister."""

    def set_eyes(self, value):
        self.eyes = value

    def get_eyes(self):
        return self.eyes

    def set_hairs(self, value):
        self.hairs = value

    def get_hairs(self):
        return self.hairs
