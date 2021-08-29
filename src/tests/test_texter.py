from src.model.lovecraft_texter import LovecraftTexter
from src.exceptions.stumped_lovecraft_exception import StumpedLovecraftException

class TexterTest:
    DATAPATH = "/Users/elizavetapertseva/Documents/Lovecraft/LovecraftText/src/model/data/lovecraft_corpus.txt"
    @staticmethod
    def run_tests():
        TexterTest.test_model_with_numbers()
        TexterTest.test_model_with_gibberish()
        TexterTest.test_model_with_simple_subject()
        TexterTest.test_model_with_greeting()
        TexterTest.test_model_with_question()
        TexterTest.test_model_with_insult()
        TexterTest.test_model_with_complex_subject()
        TexterTest.test_model_with_multiple_subjects()

    @staticmethod
    def test_model_with_greeting():
        greeting = "Hello there!"
        texter = LovecraftTexter(TexterTest.DATAPATH)
        response = texter.respond(greeting)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_simple_subject():
        simple_subject = "My name is Dog"
        texter = LovecraftTexter(TexterTest.DATAPATH)
        response = texter.respond(simple_subject)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_multiple_subjects():
        multiple_subjects = "My friends Anna and Sarah like reading your books"
        texter = LovecraftTexter(TexterTest.DATAPATH)
        response = texter.respond(multiple_subjects)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_question():
        question = "How are you today dear?"
        texter = LovecraftTexter(TexterTest.DATAPATH)
        response = texter.respond(question)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_insult():
        insult = "Your nose is over sized"
        texter = LovecraftTexter(TexterTest.DATAPATH)
        response = texter.respond(insult)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_complex_subject():
        complex_subject = "UC San Diego is a University in San Diego"
        texter = LovecraftTexter(TexterTest.DATAPATH)
        response = texter.respond(complex_subject)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_gibberish():
        gibberish = "Blah blah dofhdso;hf beep kewl"
        texter = LovecraftTexter(TexterTest.DATAPATH)
        response = texter.respond(gibberish)
        print(response)
        assert isinstance(response, str) and response is not None


    @staticmethod
    def test_model_with_numbers():
        CAUGHT_EXCEPTION = True
        numbers = 12345
        texter = LovecraftTexter(TexterTest.DATAPATH)
        try:
            response = texter.respond(numbers)
            assert not CAUGHT_EXCEPTION
        except StumpedLovecraftException as e:
            assert CAUGHT_EXCEPTION

if __name__ == "__main__":
    TexterTest.run_tests()