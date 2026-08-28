# seconds_to_time

Реализовать функцию `seconds_to_time(total: int) -> tuple[int, int, int]`,
которая переводит число секунд в тройку «часы, минуты, секунды».

## Сигнатура

```python
def seconds_to_time(total: int) -> tuple[int, int, int]: ...
```

## Примеры

```python
seconds_to_time(0)  # (0, 0, 0)
seconds_to_time(59)  # (0, 0, 59)
seconds_to_time(60)  # (0, 1, 0)
seconds_to_time(3661)  # (1, 1, 1)
seconds_to_time(86400)  # (24, 0, 0)
```

Часы не ограничены сутками: для 86400 секунд ответ `(24, 0, 0)`, а не
`(0, 0, 0)`. Аргумент неотрицателен.
