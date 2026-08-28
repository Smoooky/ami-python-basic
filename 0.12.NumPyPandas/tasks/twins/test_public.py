import numpy as np
import pandas as pd
import pytest
from twins import (
    FEATURES,
    distances,
    features,
    load,
    most_similar,
    odd_one_out,
    standardize,
)


def test_load_and_features() -> None:
    table = load()
    assert isinstance(table, pd.DataFrame)
    matrix = features(table, FEATURES)
    assert matrix.shape == (192, 3)
    assert matrix.dtype == np.float64


def test_features_checks_the_columns() -> None:
    table = load()
    with pytest.raises(KeyError):
        features(table, ["нет такой колонки"])
    with pytest.raises(ValueError):
        features(table, [])


def test_standardize() -> None:
    matrix = standardize(features(load(), FEATURES))
    assert np.allclose(matrix.mean(axis=0), 0.0)
    assert np.allclose(matrix.std(axis=0), 1.0)


def test_standardize_of_a_constant_column() -> None:
    matrix = np.array([[1.0, 5.0], [3.0, 5.0]])
    result = standardize(matrix)
    assert np.allclose(result[:, 1], 0.0)
    assert np.allclose(result[:, 0], [-1.0, 1.0])


def test_distances() -> None:
    matrix = np.array([[0.0, 0.0], [3.0, 4.0]])
    result = distances(matrix)
    assert result.shape == (2, 2)
    assert np.allclose(result, [[0.0, 5.0], [5.0, 0.0]])


def test_most_similar() -> None:
    table = load()
    assert most_similar(table, "Japan", 3) == ["Italy", "Portugal", "Greece"]
    assert most_similar(table, "Niger", 1) == ["Mali"]


def test_a_country_is_never_similar_to_itself() -> None:
    table = load()
    assert "Japan" not in most_similar(table, "Japan", 10)
    assert most_similar(table, "Japan", 0) == []


def test_unknown_country() -> None:
    with pytest.raises(KeyError):
        most_similar(load(), "Атлантида", 3)


def test_odd_one_out() -> None:
    table = load()
    assert odd_one_out(table, ["Japan", "Italy", "Germany", "Niger"]) == "Niger"
    assert odd_one_out(table, ["Niger", "Somalia", "Chad", "Japan"]) == "Japan"
    with pytest.raises(ValueError):
        odd_one_out(table, ["Japan", "Italy"])
