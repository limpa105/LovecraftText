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
    def _add_masks(text_lst: list, location: list) -> list:
        text_lst[location] = "[MASK]"
        return text_lst

    @staticmethod
    def add_mask_at_random(text: str) -> list:
        """
        Adds a mask in a random location within a string
        :param text: a string which will be masked
        :return: a masked string
        """
        # Splitting text so that it can be tokenized
        word_list = text.split(" ")
        spacy_model = spacy.load('en')
        doc = spacy_model(text)
        # We want to maintain pobj tokens and punctuation - does not make sense to replace as changes subject
        not_to_replace = [tok for tok in doc if (tok.dep_ == "pobj" or tok.dep_ == "punct")]
        i = random.randint(0, len(str)-1)
        iters = 0 # To avoid inifinite loop if all word are irreplacable
        while word_list[i] in not_to_replace:
            iters+=1
            i = random.randint(0, len(str)-1)
            if (iters > 5):
                i = 0
                break
        location = i
            
        # Replacing location at random
        return Preprocessor._add_masks(word_list, location)

    def find_similar_sentence(text: str, corpus_list: list) -> list:
        # Defining a spacy model to label entities
        spacy_model = spacy.load('en')
        doc = spacy_model(text)

        # Defining important tokens
        important = [tok for tok in doc if (tok.dep_ == "pobj")]
        if important == []:
            important = [tok for tok in doc if (tok.dep_ == "ROOT")]

        # Choosing one important token at random
        chosen_important = important[random.randint(0,len(important))]

        # Matching up
        # TODO: optimize
        random.shuffle(corpus_list)
        for sen in corpus_list:
            if chosen_important in sen:
                return sen

        # if no match is found return random
        return corpus_list[random.randint(0, len(corpus_list))]





