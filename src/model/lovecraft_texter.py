from src.model.lovecraft_model import LovecraftModel
from src.processing.preprocess import Preprocessor
import random, copy
import nltk
from nltk.corpus import words
from src.exceptions.stumped_lovecraft_exception import StumpedLovecraftException


class LovecraftTexter:
    """Defines API for a texter object which text like Lovecraft"""
    def __init__(self, data_path:str):
        self.model = LovecraftModel()
        self.data = LovecraftTexter._load_data(data_path)
        self._preprocess()

    @staticmethod
    def _load_data(data_path: str):
        """
        Loads data given datapath
        :param data_path: A path with which to access the data
        :return: String with data from datapath
        """
        # path validation
        assert isinstance(data_path, str), "data path must be a string"
        file = open(data_path, "r")
        data = file.read()
        file.close()
        return data

    def __copy__(self):
        """prototype pattern"""
        return copy.deepcopy(self)

    def _preprocess(self):
        self.processed_data = Preprocessor.preprocess_text(self.data)

    def validate_message(self, message: str):
        """
        Checks that the message is in English and not Gibberish
        :param message: the message inputed
        """
        # Input validation for non-string inputs
        if message is None or len(message) == 0 or not isinstance(message, str):
            raise StumpedLovecraftException()

    def respond(self, message: str) -> str:
        """
        Responds to a given input message
        :param message: A message to respond to
        :return: Text tokenized into sentences
        """
        # Input validation
        self.validate_message(message)
        message = message.replace("your", "mine").replace("you", "I")

        # Obtaining closest sentence
        closest_sentence = (Preprocessor.find_similar_sentence(message, self.processed_data))

        # Randomizing number of masks up to half the sentence
        num_masks = random.randint(0, len(closest_sentence.split(" "))//4)
        sentence = ""
        # Masking
        for i in range(num_masks):
            # Add a single mask onto text
            masked_sentence = "  ".join(Preprocessor.add_mask_at_random(closest_sentence))

            # Fill mask
            sentence = self.model.fill_masks(masked_sentence)

            # Continue while there are still masks to place
            closest_sentence = sentence

        # Return edited Lovecraft output
        return sentence
