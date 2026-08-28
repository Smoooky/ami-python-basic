# char_counts

Реализовать функцию `char_counts(text: str) -> dict[str, int]`, возвращающую
словарь «символ — сколько раз он встретился в строке».

## Сигнатура

```python
def char_counts(text: str) -> dict[str, int]: ...
```

## Примеры

```python
char_counts("abba")  # {"a": 2, "b": 2}
char_counts("aAa")  # {"a": 2, "A": 1}
char_counts("")  # {}
```

Регистр различается: `a` и `A` — разные символы. Пробелы и знаки препинания
считаются наравне с буквами.
