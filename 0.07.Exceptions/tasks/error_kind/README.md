# error_kind

Программа, которая падает раз в сутки, и программа, которая падает раз в
секунду, чинятся по-разному. Чтобы это различать, ошибки не просто печатают в
журнал — их считают по категориям: сколько было обращений к несуществующему
ключу, сколько отказов при работе с файлами, сколько битых данных от
пользователя. Полученная сводка сразу говорит, куда смотреть.

Категорию не нужно придумывать: она уже закодирована в иерархии исключений.
`IndexError` и `KeyError` — оба наследники `LookupError`, потому что это одна и
та же беда «искал и не нашёл». `FileNotFoundError` и `ConnectionResetError` —
оба `OSError`, потому что за ними стоит внешний мир. Классификатор, который
перечисляет конкретные классы, сломается на первом же наследнике;
классификатор, который смотрит на базовые классы, переживёт и чужие исключения.

Набор категорий закрыт и известен заранее, поэтому это не строки, а перечисление
`ErrorKind` — оно уже написано в заготовке. Опечатка в строке `"artihmetic"`
никого не смутит, и одна категория молча разъедется на две; опечатка в
`ErrorKind.ARITHMETC` — это `AttributeError` сразу же.

## Что реализовать

* `error_kind(error: BaseException) -> ErrorKind` — категория ошибки;
* `is_retryable(error: BaseException) -> bool` — имеет ли смысл повторить
  операцию. Повторяют только обрывы связи (`ConnectionError`) и таймауты
  (`TimeoutError`) вместе с их наследниками;
* `error_summary(errors: list[BaseException]) -> dict[ErrorKind, int]` — сколько
  ошибок каждой категории встретилось. Категории, которых в списке не было, в
  словарь не попадают. Ключи — члены `ErrorKind`, а не строки.

| Категория | Какие исключения | Примеры |
|---|---|---|
| `FATAL` | наследники `BaseException`, но **не** `Exception` | `KeyboardInterrupt`, `SystemExit`, `GeneratorExit` |
| `LOOKUP` | `LookupError` | `IndexError`, `KeyError` |
| `ARITHMETIC` | `ArithmeticError` | `ZeroDivisionError`, `OverflowError` |
| `OS` | `OSError` | `FileNotFoundError`, `PermissionError`, `TimeoutError` |
| `VALUE` | `ValueError` | `ValueError`, `UnicodeDecodeError` |
| `TYPE` | `TypeError` | `TypeError` |
| `OTHER` | всё остальное | `AttributeError`, `RuntimeError`, `UserWarning` |

Категория определяется по классу и всем его базовым классам, а не по имени:
наследник `KeyError` из чужой библиотеки — это `LOOKUP`. Порядок проверок здесь
такой же важный, как порядок блоков `except`: начать с `Exception` бессмысленно,
под него подходит почти всё, и любая ошибка окажется в `OTHER`.

`is_retryable` — отдельный вопрос, а не уточнение категории. `TimeoutError`
относится к `OS` и при этом достоин повтора; `FileNotFoundError` тоже `OS`, но
повторять его бесполезно.

## Примеры

```python
error_kind(KeyError("user"))  # ErrorKind.LOOKUP
error_kind(ZeroDivisionError())  # ErrorKind.ARITHMETIC
error_kind(FileNotFoundError())  # ErrorKind.OS
error_kind(TimeoutError())  # ErrorKind.OS
error_kind(ValueError("плохой ввод"))  # ErrorKind.VALUE
error_kind(AttributeError())  # ErrorKind.OTHER
error_kind(KeyboardInterrupt())  # ErrorKind.FATAL

error_kind(KeyError()).value  # "lookup" — подпись для сводки

is_retryable(ConnectionResetError())  # True
is_retryable(TimeoutError())  # True
is_retryable(FileNotFoundError())  # False

error_summary([KeyError(), IndexError(), TypeError()])
# {ErrorKind.LOOKUP: 2, ErrorKind.TYPE: 1}

error_summary([])  # {}
```
