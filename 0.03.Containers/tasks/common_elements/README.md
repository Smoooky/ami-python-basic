# common_elements

Реализовать функцию `common_elements(a: list[int], b: list[int]) -> list[int]`,
возвращающую значения, встречающиеся в обоих списках, — по одному разу, в
порядке возрастания.

## Сигнатура

```python
def common_elements(a: list[int], b: list[int]) -> list[int]: ...
```

## Примеры

```python
common_elements([1, 2, 3], [2, 3, 4])  # [2, 3]
common_elements([1, 1, 2], [2, 2, 1])  # [1, 2]
common_elements([1, 2], [3, 4])  # []
common_elements([], [1])  # []
```

Повторы внутри каждого списка на результат не влияют.
