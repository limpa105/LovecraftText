import pytest
from model.lovecraft_texter import LovecraftTexter
from exceptions.stumped_lovecraft_exception

def test_model_with_greeting():
    greeting = "Hello there!"
    texter = LovecraftTexter()
    response = texter.respond(greeting)
    print("response: ", response)
    assert isinstance(response, str) and response is not None


def test_model_with_simple_subject():
    simple_subject = "My name is Bob"
    texter = LovecraftTexter()
    response = texter.respond(simple_subject)
    print("response: ", response)
    assert isinstance(response, str) and response is not None


def test_model_with_multiple_subjects():
    multiple_subjects = " My friends Anna and Sarah like reading your books"
    texter = LovecraftTexter()
    response = texter.respond(multiple_subjects)
    print("response: ", response)
    assert isinstance(response, str) and response is not None



def test_model_with_question():
    question = "How are you today dear Lovecraft?"
    texter = LovecraftTexter()
    response = texter.respond(question)
    print("response: ", response)
    assert isinstance(response, str) and response is not None


def test_model_with_insult():
    insult = "Your feet are oversized!"
    texter = LovecraftTexter()
    response = texter.respond(insult)
    print("response: ", response)
    assert isinstance(response, str) and response is not None


def test_model_with_complex_subject():
    complex_subject = "UC San Diego is a University in San Diego"
    texter = LovecraftTexter()
    response = texter.respond(complex_subject)
    print("response: ", response)
    assert isinstance(response, str) and response is not None


def test_model_with_gibberish():
    CAUGHT_EXCEPTION = True
    gibberish = "Blah blah dofhdso;hf beep kewl"
    texter = LovecraftTexter()
    try:
        response = texter.respond(gibberish)
        assert not CAUGHT_EXCEPTION
    except StumpedLovecraftException as e:
        assert CAUGHT_EXCEPTION


def test_model_with_numbers():
    CAUGHT_EXCEPTION = True
    numbers = 12345
    texter = LovecraftTexter()
    try:
        response = texter.respond(numbers)
        assert not CAUGHT_EXCEPTION
    except StumpedLovecraftException as e:
        assert CAUGHT_EXCEPTION

