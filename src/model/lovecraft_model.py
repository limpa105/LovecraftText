from transformers import pipeline
import random


class LovecraftModel:
    """Pretrained HuggingFace BERT model which serves modified Lovecraft sentences as outputs"""

    def __init__(self):
        """Builds pretrained instance for one-time loading"""
        # Building pipeline so that does not rebuild at fill-time
        self.unmasker = pipeline('fill-mask', model='bert-base-uncased')

    def fill_masks(self, masked_text: str):
        """
        Uses pre-trained BERT mask-filler and selects chosen sentence by randomly sampling
        from possibilities with weight distribution
        :param masked_text: an input string
        :return: a sentence with generated text
        """
        # unmasking
        result = self.unmasker(masked_text)
        sequences = [item['sequence'] for item in result]

        # Building standardized discrete probability distribution for potential fill choices
        weights = [item['score'] for item in result]
        weights = [weight/sum(weights) for weight in weights]

        # Selecting sentence using distribution
        selected_sentence = random.choices(sequences, weights=weights, k= 1)[0]

        # Post processing and return
        selected_sentence = selected_sentence.replace("[CLS]", "").replace("[SEP]", "")
        return selected_sentence

