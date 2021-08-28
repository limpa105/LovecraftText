import nltk
import random
import spacy


class Preprocessor:

    @staticmethod
    def preprocess_text(text: str) -> list:
        """
        Tokenizes filetext into a list of sentences
        :param text: A piece of text to tokenize into sentences
        :return: Text tokenized into sentences
        """
        tokenized_sent_text = nltk.sent_tokenize(text)
        return tokenized_sent_text

    @staticmethod
    def _add_masks(text_lst: list, locations: list) -> str:
        for i in locations:
            text_lst[i] = "[MASK]"
        return text_lst

    @staticmethod
    def add_masks_at_random(text: str, num_masks: int) -> str:
        word_list = text.split(" ")
        spacy_model = spacy.load('en')
        doc = spacy_model(text)
        # We want to maintain pobj tokens and punctuation - does not make sense to replace as changes subject
        not_to_replace = [tok for tok in doc if (tok.dep_ == "pobj" or tok.dep_ == "punct")]
        locations = [random.randint(0, len(text) - 1) for i in num_masks if word_list[i] not in not_to_replace]
        return Preprocessor._add_masks(word_list, locations)

    def find_similar_sentences(self, text: str, corpus_list: list) -> list:
        pass



