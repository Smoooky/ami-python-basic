# rectangle

Реализовать функцию `rectangle(a: float, b: float) -> tuple[float, float]`,
которая по длинам сторон прямоугольника возвращает пару «площадь, периметр»
именно в этом порядке.

## Сигнатура

```python
def rectangle(a: float, b: float) -> tuple[float, float]: ...
```

## Примеры

```python
rectangle(2, 3)  # (6, 10)
rectangle(1, 1)  # (1, 4)
rectangle(2.5, 4.0)  # (10.0, 13.0)
```

Стороны неотрицательны. Проверять корректность аргументов не нужно.
