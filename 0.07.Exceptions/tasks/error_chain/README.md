# error_chain

Настоящая причина падения почти никогда не совпадает с тем, что видно на верхнем
уровне. Пользователь получает `RuntimeError: не удалось сохранить профиль`, а на
самом деле на диске кончилось место. Между этими двумя фактами — три слоя кода,
каждый из которых перевёл ошибку на свой язык.

Python сохраняет всю цепочку. У каждого исключения есть два поля со ссылкой на
предыдущее, и разница между ними принципиальна:

* `__cause__` — заполняется при `raise ... from ...`. Автор кода **явно
  заявил**: вот настоящая причина;
* `__context__` — заполняется автоматически, если новое исключение возникло
  внутри блока `except`. Никто ничего не заявлял, связь получилась случайно и
  часто означает баг в обработчике;
* `__suppress_context__` — становится `True` при любом `raise ... from ...`, в
  том числе при `raise ... from None`, которым связь обрывают намеренно.

## Что реализовать

* `error_chain(error: BaseException) -> list[BaseException]` — цепочка от
  переданного исключения к первопричине. Первый элемент — само `error`;
* `root_cause(error: BaseException) -> BaseException` — последний элемент
  цепочки. Для исключения без предыстории это оно само;
* `explain(error: BaseException) -> str` — цепочка в виде текста для лога.

Следующим для очередного исключения считается `__cause__`, если он не `None`;
иначе `__context__`, если `__suppress_context__` равен `False`; иначе цепочка
кончилась. `__cause__` проверяется первым не для красоты: явно указанная
причина важнее случайно подхваченного контекста.

Цепочку можно замкнуть в кольцо, присвоив полям что угодно вручную. Обход обязан
такое пережить: исключение, которое уже попало в цепочку, второй раз в неё не
добавляется, и обход на нём останавливается.

`explain` даёт одну строку на исключение, строки соединены `"\n"`. Строка уровня
`i` начинается с отступа в `2 * i` пробелов, дальше приставка, дальше
`"<имя класса>: <текст>"`, где текст — это `str(error)`: у `KeyError('profile')`
он равен `"'profile'"`, а у исключения без сообщения пустой. Приставки: для
самого исключения её нет, для перехода по `__cause__` — `причина: `, по
`__context__` — `в процессе: `.

## Примеры

```python
try:
    try:
        1 / 0
    except ZeroDivisionError as error:
        raise ValueError("плохой делитель") from error
except ValueError as error:
    top = error

error_chain(top)  # [ValueError, ZeroDivisionError]
root_cause(top)  # исходный ZeroDivisionError
print(explain(top))
# ValueError: плохой делитель
#   причина: ZeroDivisionError: division by zero
```

```python
try:
    try:
        raise KeyError("host")
    except KeyError:
        raise RuntimeError("обработчик сам сломался")  # from не указан
except RuntimeError as error:
    top = error

print(explain(top))
# RuntimeError: обработчик сам сломался
#   в процессе: KeyError: 'host'
```

```python
try:
    try:
        raise KeyError("host")
    except KeyError:
        raise RuntimeError("наружу показываем только это") from None
except RuntimeError as error:
    top = error

error_chain(top)  # [RuntimeError] — связь оборвана явно
explain(top)  # "RuntimeError: наружу показываем только это"
explain(ValueError())  # "ValueError: " — сообщения нет, двоеточие есть
```
