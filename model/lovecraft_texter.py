from lovecraft_model import LovecraftModel
from processing.preprocess import Preprocessor

class LovecraftTexter:
    """"""
    def __init__(self):
        self.model = LovecraftModel()

    def _load_data(self, data_path: str):
        pass

    def _preprocess(self):
        Preprocessor.preprocess_text(self.data)

    def respond(self, message: str):
        pass