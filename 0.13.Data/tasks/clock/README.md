# clock

В `datetime` два типа для одного и того же: `date` — день без времени,
`datetime` — момент внутри дня. В одну программу они попадают вперемешку: одно
поле пришло из формы датой, другое из файла моментом. Дальше их сравнивают, и
это работает не так, как ожидается.

Задача — набор функций, которые с такой смесью справляются.

## Что реализовать

Все функции принимают `date` и `datetime`. Что-либо ещё — `TypeError`.
Осведомлённое время (с часовым поясом) — `ValueError`: здесь работаем только с
наивным.

* `is_datetime(moment)` — момент ли это;
* `is_date(moment)` — день ли это, без времени;
* `as_datetime(moment)` — момент. Дню приписывается полночь, готовое время —
  в `MIDNIGHT` в шапке модуля;
* `as_date(moment)` — день. У момента время отбрасывается, и результат обязан
  быть именно днём;
* `same_day(first, second)` — приходятся ли оба на один день;
* `order(moments)` — список по возрастанию. Смесь допускается, день считается
  своей полночью. Возвращаются те же объекты, ничего не преобразуется; при
  совпадении моментов сохраняется исходный порядок;
* `between(first, second)` — сколько прошло от первого до второго. Если второй
  раньше, результат отрицательный, и это не ошибка.

`is_date` и `is_datetime` не могут быть оба истинны ни для какого значения.

## Примеры

```python
day = date(2026, 9, 1)
moment = datetime(2026, 9, 1, 10, 30)

is_date(day)  # True
is_date(moment)  # False
is_datetime(moment)  # True

as_datetime(day)  # datetime(2026, 9, 1, 0, 0)
as_date(moment)  # date(2026, 9, 1)
same_day(day, moment)  # True
```

```python
day == datetime(2026, 9, 1, 0, 0)  # False
day < moment  # TypeError
sorted([moment, day])  # TypeError

order([moment, day, datetime(2026, 8, 31, 23, 59)])
# [datetime(2026, 8, 31, 23, 59), date(2026, 9, 1), datetime(2026, 9, 1, 10, 30)]
```

```python
between(day, moment)  # timedelta(seconds=37800)
between(moment, day)  # timedelta(days=-1, seconds=48600)
between(day, date(2026, 9, 3))  # timedelta(days=2)
```
