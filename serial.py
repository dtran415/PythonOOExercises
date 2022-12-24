"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """ create a number generator starting with start """
        self.start = self.next = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """ return the current next number then increment it """
        res = self.next
        self.next += 1
        return res

    def reset(self):
        """ reset next number back to start """
        self.next = self.start