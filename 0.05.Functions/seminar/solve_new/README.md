# solve_new — решения задач из problems_new

Тесты лежат один раз в `problems_new/` и импортируют модули `task01_*`–`task05_*`.
Но `conftest.py` из `problems_new` ставит этот каталог первым в `sys.path`,
поэтому при запуске из `problems_new` pytest всегда находит заготовки,
а не решения.

## Проверить решения

Склеить тесты и решения в отдельном каталоге и прогнать там:

```bash
cd 0.05.Functions/seminar
rm -rf /tmp/check && mkdir /tmp/check
cp problems_new/test_*.py solve_new/*.py /tmp/check/
cd /tmp/check && python3 -m pytest -q
```

Ожидаемый результат — все тесты зелёные.

## Прогон против заготовок

Из `problems_new` те же тесты должны падать — каждая подзадача заготовки
бросает `NotImplementedError`:

```bash
cd 0.05.Functions/seminar/problems_new && python3 -m pytest -q
```
