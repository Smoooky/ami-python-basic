"""Решение задачи 5 (problems_new/5_buffer.py)."""


def histogram(view: memoryview) -> list[int]:
    """Итерация по окну отдаёт байты — копии не появляется."""
    counts = [0] * 256
    for byte in view:
        counts[byte] += 1
    return counts


def mirror_window(view: memoryview) -> None:
    """Обмен симметричных индексов меняет сам буфер, без промежуточной копии."""
    for i in range(len(view) // 2):
        view[i], view[-1 - i] = view[-1 - i], view[i]


def most_common(view: memoryview) -> int:
    """index находит первую позицию максимума — при ничьей это меньший байт."""
    counts = histogram(view)
    return counts.index(max(counts))
