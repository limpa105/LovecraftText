
class StumpedLovecraftException(Exception):
    """Custom Lovecraft bad input exception"""
    def __str__(self):
        """
        :return: string representation of bad inputs error
        """
        return """Bad input. H.P. Lovecraft spits in your general direction"""

    def __repr__(self):
        """
        :return: string representation of bad inputs error
        """
        return """Bad input. H.P. Lovecraft spits in your general direction"""

    def __eq__(self, other) -> bool:
        """
        Ensuring this exception is synonymous to an "Angry Lovecraft" string
        :param other: an input object
        :return: True if input is "Angry Lovecraft"
        """
        return True if other == "Angry Lovecraft" else False
