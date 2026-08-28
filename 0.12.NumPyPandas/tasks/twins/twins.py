from pathlib import Path

import numpy as np
import numpy.typing as npt
import pandas as pd

DATA = Path(__file__).parent / "global_population_stats_2024.csv"

COUNTRY = "Country"
YOUNG = "Population Aged 0 to 14 (%)"
OLD = "Population Aged 60 and Over (%)"
SEX_RATIO = "Sex ratio (males per 100 females)"

# По этим трём числам и решаем, похожи ли страны друг на друга.
FEATURES = [YOUNG, OLD, SEX_RATIO]


def load() -> pd.DataFrame:
    raise NotImplementedError("Implement me")


def features(table: pd.DataFrame, columns: list[str]) -> npt.NDArray[np.float64]:
    raise NotImplementedError("Implement me")


def standardize(matrix: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    raise NotImplementedError("Implement me")


def distances(matrix: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    raise NotImplementedError("Implement me")


def most_similar(table: pd.DataFrame, country: str, count: int) -> list[str]:
    raise NotImplementedError("Implement me")


def odd_one_out(table: pd.DataFrame, countries: list[str]) -> str:
    raise NotImplementedError("Implement me")
