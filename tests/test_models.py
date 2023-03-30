import pytest
from models.tokenizer import Tokenizer
from models.speech_synthesis import SpeechSynthesis

pytest.main()


def test_tokenizer_init():
    tokenizer = Tokenizer()
    assert tokenizer.encoding_name == "cl100k_base"
    assert tokenizer.enc.name == "cl100k_base"


def test_tokenizer_for_model():
    tokenizer = Tokenizer(encoding_name="gpt-4", for_model=True)
    assert tokenizer.encoding_name == "gpt-4"
    assert tokenizer.enc.name == "cl100k_base"


def test_tokenizing_strings():
    tokenizer = Tokenizer()
    assert tokenizer.enc.decode(tokenizer.enc.encode("Hello, world!")) == "Hello, world!"


def test_decoding_single_token():
    tokenizer = Tokenizer()
    assert (tokenizer.enc.decode_single_token_bytes(tokenizer.enc.encode("Hello, world!")[0])).decode() == "Hello"


def test_init_defaults():
    speech_synthesis = SpeechSynthesis()
    assert speech_synthesis.model_name is not None
    assert speech_synthesis.speaker is not None
