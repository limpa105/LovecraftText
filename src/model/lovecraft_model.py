from transformers import pipeline
import random
import spacy



class LovecraftModel:

    def __init__(self):
        """Builds pretrained instance for one-time loading"""
        self.unmasker = pipeline('fill-mask', model='bert-base-uncased')

    def fill_masks(self, masked_text: str):
        """
        Uses pre-trained BERT mask-filler and selects chosen sentence by randomly sampling
        from possibilities with weight distribution
        :param masked_text: an input string
        :return: a sentence with generated text
        """
        result = self.unmasker(masked_text)
        sequences = [item['sequence'] for item in result]
        weights = [item['score'] for item in result]
        weights = [weight/sum(weights) for weight in weights]
        selected_sentence = random.choices(sequences, weights=weights, k= 1)[0]
        selected_sentence = selected_sentence.replace("[CLS]", "").replace("[SEP]", "")
        return selected_sentence

