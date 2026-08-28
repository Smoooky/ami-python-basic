# order_status

Статус заказа — не просто метка. Между статусами разрешены не любые переходы:
оплаченный заказ можно доставить или отменить, но нельзя вернуть в состояние
«новый», а из доставленного не ведёт никуда. Набор таких правил называется
конечным автоматом.

Реализовать перечисление `OrderStatus` с четырьмя членами:

| Член | Значение |
|---|---|
| `NEW` | `"new"` |
| `PAID` | `"paid"` |
| `DELIVERED` | `"delivered"` |
| `CANCELLED` | `"cancelled"` |

Разрешённые переходы:

| Из состояния | Куда можно перейти |
|---|---|
| `NEW` | `PAID`, `CANCELLED` |
| `PAID` | `DELIVERED`, `CANCELLED` |
| `DELIVERED` | никуда |
| `CANCELLED` | никуда |

## Что реализовать

* `next_states(self) -> set["OrderStatus"]` — множество состояний, достижимых
  за один переход. Изменение возвращённого множества не должно влиять на
  таблицу переходов;
* `can_move_to(self, other: "OrderStatus") -> bool` — разрешён ли переход в
  указанное состояние;
* `is_final(self) -> bool` — состояние, из которого нет ни одного перехода;
* статический метод `is_valid_path(states: list["OrderStatus"]) -> bool` —
  каждый переход в цепочке разрешён. Пустой путь и путь из одного состояния
  допустимы.

Перехода состояния в само себя нет ни у одного члена.

## Примеры

```python
OrderStatus.NEW.value  # "new"
OrderStatus("paid")  # OrderStatus.PAID

OrderStatus.NEW.can_move_to(OrderStatus.PAID)  # True
OrderStatus.NEW.can_move_to(OrderStatus.DELIVERED)  # False

OrderStatus.PAID.next_states()  # {DELIVERED, CANCELLED}
OrderStatus.DELIVERED.next_states()  # set()
OrderStatus.DELIVERED.is_final()  # True

OrderStatus.is_valid_path([OrderStatus.NEW, OrderStatus.PAID, OrderStatus.DELIVERED])  # True
OrderStatus.is_valid_path([OrderStatus.NEW, OrderStatus.DELIVERED])  # False
OrderStatus.is_valid_path([])  # True
```
