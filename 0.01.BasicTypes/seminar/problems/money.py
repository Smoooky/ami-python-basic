"""Задача 2. Деньги и точность float.

Главное правило: сумму денег нельзя хранить во float. Здесь цена приходит
строкой вида "12.30", хранится в копейках целым числом и собирается обратно
склейкой строк.
"""


def to_cents(price: str) -> int:
    """Цена из строки в копейки: "12.30" -> 1230.

    Рубли и копейки разделены точкой, копеек всегда ровно две цифры, цена
    неотрицательна. Через float переводить нельзя — он потеряет точность.
    """
    raise NotImplementedError("Implement me")


def format_price(cents: int) -> str:
    """Копейки обратно в строку: 1230 -> "12.30", 5 -> "0.05".

    Копеек всегда ровно две цифры, поэтому однозначное число нужно дополнить
    нулём слева. Достаточно склейки строк и среза.
    """
    raise NotImplementedError("Implement me")


def add_prices(first: str, second: str) -> str:
    """Сумма двух цен в том же виде: "12.30" и "0.70" -> "13.00"."""
    raise NotImplementedError("Implement me")


def round_half_up(x: float) -> int:
    """Округление «половина вверх», к которому привыкли в школе.

    Встроенный round округляет половину к чётному: round(2.5) == 2. Здесь
    нужно 3. Отрицательные: round_half_up(-0.5) == 0, round_half_up(-1.5) == -1.
    """
    raise NotImplementedError("Implement me")


def close_enough(x: float, y: float) -> bool:
    """Совпадают ли два float с точностью до погрешности вычислений.

    close_enough(0.1 + 0.2, 0.3) — True, хотя == даёт False.
    """
    raise NotImplementedError("Implement me")
