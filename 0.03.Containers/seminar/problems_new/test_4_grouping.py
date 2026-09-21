from importlib import import_module

grouping = import_module("4_grouping")


def test_by_first_letter() -> None:
    assert grouping.by_first_letter(["кот", "кит", "як", "ёж"]) == {
        "к": ["кот", "кит"],
        "я": ["як"],
        "ё": ["ёж"],
    }
    assert grouping.by_first_letter([]) == {}


def test_by_first_letter_keeps_the_input_order_and_duplicates() -> None:
    assert grouping.by_first_letter(["як", "кот", "як"]) == {"я": ["як", "як"], "к": ["кот"]}


def test_word_counts() -> None:
    assert grouping.word_counts("кот пёс кот") == {"кот": 2, "пёс": 1}
    assert grouping.word_counts("") == {}
    assert grouping.word_counts("кот") == {"кот": 1}


def test_word_counts_is_case_sensitive() -> None:
    assert grouping.word_counts("Кот кот") == {"Кот": 1, "кот": 1}


def test_keys_by_value() -> None:
    assert grouping.keys_by_value({"а": 1, "б": 2, "в": 1}) == {1: ["а", "в"], 2: ["б"]}
    assert grouping.keys_by_value({}) == {}


def test_keys_by_value_keeps_the_dict_order() -> None:
    assert grouping.keys_by_value({"б": 1, "а": 1}) == {1: ["б", "а"]}
