from lovecraft_model import LovecraftModel
from processing.preprocess import Preprocessor
import random, copy
import nltk
from nltk.corpus import words
from exceptions.stumped_lovecraft_exception import StumpedLovecraftException

class LovecraftTexter:
    """Defines API for a texter object which text like Lovecraft"""
    def __init__(self, data_path:str):
        self.model = LovecraftModel()
        self.data = self._load_data(data_path)

    def _load_data(self, data_path: str):
        """
        Loads data given datapath
        :param data_path: A path with which to access the data
        :return: String with data from datapath
        """
        # path validation
        assert isinstance(data_path, str), "data path must be a string"
        try:
            file = open(data_path, "r")
        except:
            assert False, "Invalid filepath"
        data = file.read()
        file.close()
        return data

    @property
    def data(self):
        return self.data

    @data.getter
    def data(self,):
        if self.data is not None:
            return self.data

    @data.setter
    def data(self, new_data: str):
        if isinstance(new_data, str):
            self.data = new_data

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
        tokens = nltk.word_tokenize(message)
        for word in tokens:
            # Validating word actually in English language, if not raising exception
            if word not in words.words():
                raise StumpedLovecraftException()

    def respond(self, message: str):
        """
        Responds to a given input message
        :param message: A message to respo
        :return: Text tokenized into sentences
        """
        # Input validation
        self.validate_message(message)

        # Obtaining closest sentence
        closest_sentence = " ".join((Preprocessor.find_similar_sentence(self.processed_data, message)))

        # Randomizing number of masks up to half the sentence
        num_masks = random.randint(0, len(closest_sentence)//2)
        sentence = ""
        # Masking
        for i in range(num_masks):
            masked_sentence = "  ".join(Preprocessor.add_mask_at_random(closest_sentence))
            sentence = self.model.fill_masks(masked_sentence)
        return sentence