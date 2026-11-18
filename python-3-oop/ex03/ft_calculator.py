class calculator:
    def __init__(self, vector):
        """ Initialises list of strings as floats

        Args:
            vector (list): list of strings
        """
        self.vector = [float(x) for x in vector]

    def __add__(self, object):
        """ Adds a float to our list

        Args:
            object (float)
        """
        self.vector = [float(object) + x for x in self.vector]
        print(self.vector)

    def __mul__(self, object):
        """ Multiplication on list

        Args:
            object (float)
        """
        self.vector = [float(object) * x for x in self.vector]
        print(self.vector)

    def __sub__(self, object):
        """ Subtracts from List

        Args:
            object (float)
        """
        self.vector = [x - float(object) for x in self.vector]
        print(self.vector)

    def __truediv__(self, object):
        """ Divides list by float
            Raises Error for Zero division

        Args:
            object (float)
        """
        if float(object) == 0:
            raise (ZeroDivisionError)
        self.vector = [x / float(object) for x in self.vector]
        print(self.vector)
