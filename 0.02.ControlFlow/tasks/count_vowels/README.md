# count_vowels

Реализовать функцию `count_vowels(text: str) -> int`, считающую количество
гласных букв в строке. Учитываются гласные латиницы (`a e i o u`) и кириллицы
(`а е ё и о у ы э ю я`). Регистр не важен.

## Сигнатура

```python
def count_vowels(text: str) -> int: ...
```

## Примеры

```python
count_vowels("hello")  # 2
count_vowels("Привет")  # 2
count_vowels("XYZ")  # 0
count_vowels("")  # 0
```

Символы, не являющиеся буквами, просто не считаются.
