import unicodedata

from text import byte_size, canonical, codepoints, same_text

COMPOSED = unicodedata.normalize("NFC", "café")
DECOMPOSED = unicodedata.normalize("NFD", "café")


def test_codepoints() -> None:
    assert codepoints("AB") == (65, 66)
    assert codepoints("") == ()
    assert codepoints("я") == (1103,)


def test_codepoints_returns_a_tuple() -> None:
    assert isinstance(codepoints("AB"), tuple)


def test_byte_size() -> None:
    assert byte_size("abc", "utf-8") == 3
    assert byte_size("ы", "utf-8") == 2
    assert byte_size("ы", "cp1251") == 1
    assert byte_size("", "utf-8") == 0


def test_byte_size_is_not_the_same_as_length() -> None:
    assert len("привет") == 6
    assert byte_size("привет", "utf-8") == 12


def test_canonical() -> None:
    assert canonical("  Привет  ") == "привет"
    assert canonical("STRASSE") == "strasse"
    assert canonical("") == ""


def test_canonical_folds_the_german_sharp_s() -> None:
    assert canonical("straße") == "strasse"


def test_canonical_normalizes_diacritics() -> None:
    # Две записи одной и той же буквы должны схлопнуться в одну.
    assert len(COMPOSED) == 4
    assert len(DECOMPOSED) == 5
    assert canonical(COMPOSED) == canonical(DECOMPOSED)


def test_same_text() -> None:
    assert same_text("Привет", "привет  ") is True
    assert same_text(COMPOSED, DECOMPOSED) is True
    assert same_text("привет", "прощай") is False
    assert same_text("", "   ") is True
