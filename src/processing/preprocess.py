import nltk
import random
import spacy
import en_core_web_sm


class Preprocessor:

    @staticmethod
    def preprocess_text(text: str) -> list:
        """
        Tokenizes given text into a list of sentences
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
        # Constant representing maximum iterations
        max_iters = 5

        # Splitting text so that it can be tokenized
        word_list = text.split(" ")
        spacy_model = spacy.load('en_core_web_sm')
        doc = spacy_model(text)

        # We want to maintain dobj tokens and punctuation - does not make sense to replace as changes subject
        not_to_replace = ([tok.text for tok in doc if
                          (tok.dep_ == "attr" or tok.dep_ == "dobj" or tok.dep_ == "punct")])
        i = random.randint(0, len(word_list)-1)

        # To avoid infinite loop if all word are irreplaceable
        iters = 0

        while word_list[i] in not_to_replace:
            # Generating random value to replace
            iters += 1
            i = random.randint(0, len(word_list)-1)

            # If we have exceeded maximum lost random number generations
            if iters > max_iters:
                i = 0
                break

        # Setting location post loop
        location = i
            
        # Replacing location at random
        return Preprocessor._add_masks(word_list, location)

    @staticmethod
    def find_similar_sentence(text:str, corpus_list: list) -> list:
        # Defining a spacy model to label entities
        spacy_model = spacy.load("en_core_web_sm")
        doc = spacy_model(text)

        # Defining important tokens
        important = [tok for tok in doc if (tok.dep_ == "attr")]
        if important == []:
            important = [tok for tok in doc if (tok.dep_ == "nsubj" or tok.dep_ == "pobj")]
        if important == []:
            important = [doc[0]]

        # Choosing one important token at random
        chosen_important = important[random.randint(0,len(important)-1)]

        # Matching up to Lovecraft sentence
        random.shuffle(corpus_list)
        for sen in corpus_list:
            if chosen_important.text in sen:
                return sen

        # if no match is found return random
        return corpus_list[random.randint(0, len(corpus_list))]





