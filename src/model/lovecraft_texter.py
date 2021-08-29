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
        self.data = self._load_data(data_path)
        self._preprocess()

    def _load_data(self, data_path: str):
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
        if not isinstance(message, str):
            raise StumpedLovecraftException()

    def respond(self, message: str):
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
            masked_sentence = "  ".join(Preprocessor.add_mask_at_random(closest_sentence))
            sentence = self.model.fill_masks(masked_sentence)
            closest_sentence = sentence
        return sentence