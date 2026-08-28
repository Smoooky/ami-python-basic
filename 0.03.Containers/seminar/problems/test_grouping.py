from grouping import by_length, char_counts, invert


def test_by_length() -> None:
    assert by_length(["кот", "пёс", "коза"]) == {3: ["кот", "пёс"], 4: ["коза"]}
    assert by_length([]) == {}


def test_by_length_keeps_the_input_order_and_duplicates() -> None:
    assert by_length(["як", "кот", "як"]) == {2: ["як", "як"], 3: ["кот"]}


def test_by_length_with_an_empty_word() -> None:
    assert by_length([""]) == {0: [""]}


def test_char_counts() -> None:
    assert char_counts("абба") == {"а": 2, "б": 2}
    assert char_counts("") == {}
    assert char_counts("ааа") == {"а": 3}


def test_char_counts_counts_spaces() -> None:
    assert char_counts("а б") == {"а": 1, " ": 1, "б": 1}


def test_invert() -> None:
    assert invert({"а": 1, "б": 2}) == {1: "а", 2: "б"}
    assert invert({}) == {}


def test_invert_keeps_the_last_key_of_a_repeated_value() -> None:
    assert invert({"а": 1, "б": 1}) == {1: "б"}


def test_invert_with_zero_and_negative_values() -> None:
    assert invert({"ноль": 0, "минус": -1}) == {0: "ноль", -1: "минус"}
