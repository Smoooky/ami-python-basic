import pandas as pd
import pytest
from census import (
    BAND,
    COUNTRY,
    PEOPLE,
    SHARE,
    YOUNG,
    add_female_share,
    ageing,
    band,
    load,
    lookup,
    summary,
    youngest,
)


def as_float(value: object) -> float:
    """Скаляр из pandas — в обычный float."""
    return float(value)  # type: ignore[arg-type]


def table() -> pd.DataFrame:
    return load()


def test_load() -> None:
    data = table()
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (192, 8)
    assert COUNTRY in data.columns
    assert data[COUNTRY].is_unique


def test_add_female_share() -> None:
    data = table()
    result = add_female_share(data)
    assert SHARE in result.columns
    assert SHARE not in data.columns
    russia = result.set_index(COUNTRY).loc["Russia", SHARE]
    assert round(as_float(russia), 1) == 53.6


def test_youngest() -> None:
    result = youngest(table(), 3)
    assert list(result.columns) == [COUNTRY, YOUNG]
    assert result[COUNTRY].tolist() == ["Central African Republic", "Niger", "Somalia"]
    assert youngest(table(), 0).empty


def test_ageing() -> None:
    assert ageing(table(), 28.0, 50.0) == ["Japan", "Italy", "Germany", "France"]
    assert ageing(table(), 99.0, 0.0) == []


def test_lookup() -> None:
    result = lookup(table(), ["Japan", "Russia"])
    assert result.index.tolist() == ["Japan", "Russia"]
    assert round(as_float(result.loc["Japan", PEOPLE]), 2) == 123.75
    with pytest.raises(KeyError):
        lookup(table(), ["Атлантида"])


def test_band() -> None:
    result = band(table())
    assert isinstance(result, pd.Series)
    assert len(result) == 192
    assert result.value_counts().to_dict() == {"средне": 84, "просторно": 57, "плотно": 51}


def test_summary() -> None:
    result = summary(table())
    assert list(result.index) == ["средне", "просторно", "плотно"]
    assert result.index.name == BAND
    assert list(result.columns) == ["countries", "people", "old_share"]
    assert result.loc["средне", "countries"] == 84
    assert round(as_float(result.loc["плотно", "old_share"]), 2) == 15.74


def test_youngest_checks_the_count() -> None:
    with pytest.raises(ValueError):
        youngest(table(), -1)
