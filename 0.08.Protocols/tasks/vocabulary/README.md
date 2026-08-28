# vocabulary

Словарик для заучивания слов: английское слово — перевод. Хранить такое удобно
в `dict`, но одна беда всплывает сразу же. Слово, записанное с заглавной буквы,
и оно же со строчной — для нас одно и то же слово, а для `dict` два разных
ключа:

```python
words = {"Apple": "яблоко"}
words["apple"]  # KeyError, хотя слово-то есть
```

Подчищать регистр в каждом месте, где обращаются к словарику, — гиблое дело:
рано или поздно про одно место забудут. Правило должно жить внутри самой
структуры, и отличаться от обычного словаря она должна ровно им одним: `get`,
`pop`, `update`, `setdefault`, `keys`, `in`.

`MutableMapping` из `collections.abc` предлагает ту же сделку, что `Route` в
предыдущей задаче: пять методов от вас — весь остальной словарь от него.

## Что реализовать

Класс `Vocabulary` — наследник `MutableMapping[str, str]`.

```python
from collections.abc import Iterator, MutableMapping


class Vocabulary(MutableMapping[str, str]): ...
```

* `normalize(word: str) -> str` — статический метод: слово обрезается по краям
  от пробелов и приводится к нижнему регистру. `"  Apple  "` и `"APPLE"` дают
  `"apple"`;
* `__init__(self, words: Any = ())` — словарик из обычного `dict` или из пар
  «слово, перевод»;
* `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__len__`;
* `__repr__` — `Vocabulary({'apple': 'яблоко'})`.

Перевод при записи тоже обрезается по краям от пробелов. Пустое слово (или из
одних пробелов) недопустимо: `ValueError`. Обращение к отсутствующему слову —
`KeyError`, как и положено отображению.

## Примеры

```python
Vocabulary.normalize("  Apple  ")  # "apple"

words = Vocabulary({"Apple": "яблоко", "  BOOK ": "  книга  "})

words["APPLE"]  # "яблоко"
words["book"]  # "книга" — перевод тоже обрезан
list(words)  # ["apple", "book"]
repr(words)  # "Vocabulary({'apple': 'яблоко', 'book': 'книга'})"

"APPLE" in words  # True — не писали, а работает
words.get("nope", "не знаю")  # "не знаю"
words.pop("Apple")  # "яблоко"

words.update({"Cat": "кот", "DOG": "собака"})
sorted(words.keys())  # ["book", "cat", "dog"]
words.setdefault("cat", "кошка")  # "кот" — слово уже есть, не перезаписали

Vocabulary({"a": "1"}) == Vocabulary({"A": "1"})  # True
words[""] = "перевод"  # ValueError
words["нет такого"]  # KeyError
```
