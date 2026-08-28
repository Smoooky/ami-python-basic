from word_frequency import word_frequency


def test_simple() -> None:
    assert word_frequency("дом дом") == {"дом": 2}


def test_case_and_punctuation() -> None:
    assert word_frequency("Дом, дом!") == {"дом": 2}


def test_empty() -> None:
    assert word_frequency("") == {}
