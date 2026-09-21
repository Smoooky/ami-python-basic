"""Задача 5. Окно в буфер.

`memoryview` над `bytearray` — это не копия, а окно: запись через индекс
окна меняет сам буфер. Все функции работают с уже созданным окном
и не копируют буфер целиком.
"""


def histogram(view: memoryview) -> list[int]:
    """Сколько раз каждый байт (от 0 до 255) встречается в окне.

    Ответ — список из 256 счётчиков: позиция равна значению байта.
    """
    raise NotImplementedError("Implement me")


def mirror_window(view: memoryview) -> None:
    """Развернуть байты внутри окна задом наперёд.

    Меняется сам буфер под окном; ничего не возвращается. Размер буфера
    при живом окне менять нельзя — окно держит его занятым.
    """
    raise NotImplementedError("Implement me")


def most_common(view: memoryview) -> int:
    """Самый частый байт в окне; при равенстве частот — наименьший.

    Окно непустое.
    """
    raise NotImplementedError("Implement me")
