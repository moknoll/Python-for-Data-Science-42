from abc import ABC, abstractmethod


class Character(ABC):
    """ Charachter is an abstract class.
        with:
            - first_name: str
            - is_alive: bool = Default True

    Args:
        ABC : Turns the class into an abstract class
    """
    def __init__(self, first_name: str, is_alive=True):
        """ Initialises the class

        Args:
            first_name (str): Takes a string as a first parameter
            alive (bool, optional): Defaults to True.
        """
        self.first_name: str = first_name
        self.is_alive = is_alive

    @abstractmethod
    def announce(self):
        pass

    def die(self):
        """ Kill the character, set is_alive to False """
        self.is_alive = False


class Stark(Character):
    """ Stark Is a subclass From Character.
        The class inherints the die method, aswell as the attributes

    Args: Character class
    """
    def announce(self):
        print(f"{self.first_name} was created and {self.is_alive}")
