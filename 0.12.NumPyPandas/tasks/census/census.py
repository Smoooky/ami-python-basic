from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "global_population_stats_2024.csv"

YOUNG = "Population Aged 0 to 14 (%)"
OLD = "Population Aged 60 and Over (%)"
DENSITY = "Population density"
PEOPLE = "Population(in millions)"
WOMEN = "Female Population(in millions)"
COUNTRY = "Country"
SHARE = "Female share (%)"
BAND = "Density band"


def load() -> pd.DataFrame:
    raise NotImplementedError("Implement me")


def add_female_share(table: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Implement me")


def youngest(table: pd.DataFrame, count: int) -> pd.DataFrame:
    raise NotImplementedError("Implement me")


def ageing(table: pd.DataFrame, share: float, population: float) -> list[str]:
    raise NotImplementedError("Implement me")


def lookup(table: pd.DataFrame, countries: list[str]) -> pd.DataFrame:
    raise NotImplementedError("Implement me")


def band(table: pd.DataFrame) -> pd.Series:
    raise NotImplementedError("Implement me")


def summary(table: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Implement me")
