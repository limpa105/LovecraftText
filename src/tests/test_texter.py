import pytest
from src.model.lovecraft_texter import LovecraftTexter
from src.exceptions.stumped_lovecraft_exception import StumpedLovecraftException

class TexterTest:
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
        texter = LovecraftTexter("model/data/lovecraft_corpus.txt")
        response = texter.respond(greeting)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_simple_subject():
        simple_subject = "My name is Bob"
        texter = LovecraftTexter("model/data/lovecraft_corpus.txt")
        response = texter.respond(simple_subject)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_multiple_subjects():
        multiple_subjects = "My friends Anna and Sarah like reading your books"
        texter = LovecraftTexter("model/data/lovecraft_corpus.txt")
        response = texter.respond(multiple_subjects)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_question():
        question = "How are you today dear Lovecraft?"
        texter = LovecraftTexter("model/data/lovecraft_corpus.txt")
        response = texter.respond(question)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_insult():
        insult = "Your feet are oversized!"
        texter = LovecraftTexter("model/data/lovecraft_corpus.txt")
        response = texter.respond(insult)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_complex_subject():
        complex_subject = "UC San Diego is a University in San Diego"
        texter = LovecraftTexter("model/data/lovecraft_corpus.txt")
        response = texter.respond(complex_subject)
        print("response: ", response)
        assert isinstance(response, str) and response is not None

    @staticmethod
    def test_model_with_gibberish():
        CAUGHT_EXCEPTION = True
        gibberish = "Blah blah dofhdso;hf beep kewl"
        texter = LovecraftTexter("model/data/lovecraft_corpus.txt")
        try:
            response = texter.respond(gibberish)
            assert not CAUGHT_EXCEPTION
        except StumpedLovecraftException as e:
            assert CAUGHT_EXCEPTION

    @staticmethod
    def test_model_with_numbers():
        CAUGHT_EXCEPTION = True
        numbers = 12345
        texter = LovecraftTexter("model/data/lovecraft_corpus.txt")
        try:
            response = texter.respond(numbers)
            assert not CAUGHT_EXCEPTION
        except StumpedLovecraftException as e:
            assert CAUGHT_EXCEPTION

if __name__ == "__main__":
    TexterTest.run_tests()