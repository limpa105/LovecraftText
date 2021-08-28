from lovecraft_model import LovecraftModel
from processing.preprocess import Preprocessor

class LovecraftTexter:
    """"""
    def __init__(self):
        self.preprocessor = Preprocessor()
        self.model = LovecraftModel()