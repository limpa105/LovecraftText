
class Preprocessor:

    @staticmethod
    def preprocess_text(self, text):
        from nltk.corpus import gutenberg
        jane_austen = gutenberg.sents('austen-emma.txt')
        shakespeare = gutenberg.sents('shakespeare-hamlet.txt')
        melville = gutenberg.sents('melville-moby_dick.txt')

        print(jane_austen)

    def add_masks_at_positions(self, text: str, locations: list) -> str:
        pass

    def add_masks_at_random(self, **hyperparameters) -> str:
        pass



