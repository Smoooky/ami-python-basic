# accounts

Банковские счета отличаются не тем, как хранят деньги, а тем, при каких условиях
разрешают их снять. С накопительного нельзя уйти в минус. Расчётный допускает
овердрафт — уход в минус в пределах согласованного лимита. Со срочного вклада
снять нельзя вовсе, пока не кончился срок.

Общая часть — баланс, пополнение, история операций — одинакова у всех, поэтому
описывается один раз, а различие в правилах списания задаётся потомками.

Реализовать четыре класса.

## Account

Базовый счёт.

* `__init__(self, owner: str, balance: float = 0)` — поля `owner`, `balance` и
  `history`: список записей об операциях, изначально пустой;
* `deposit(self, amount: float) -> None` — пополнение. Неположительная сумма
  недопустима: `ValueError`. Баланс увеличивается, в историю добавляется строка
  `"+<сумма>"`;
* `can_withdraw(self, amount: float) -> bool` — разрешено ли списание. У
  базового счёта правил нет, метод возбуждает `NotImplementedError`;
* `withdraw(self, amount: float) -> None` — списание. Неположительная сумма
  недопустима: `ValueError`. Если `can_withdraw` возвращает `False`, списание
  невозможно: `ValueError`. Иначе баланс уменьшается, в историю добавляется
  строка `"-<сумма>"`;
* сравнение по балансу: счета упорядочиваются, список счетов можно
  отсортировать;
* статический метод `total_balance(accounts: list["Account"]) -> float` — сумма
  балансов.

Записи в истории записываются числом как есть: `"+100"`, `"-50.5"`.

## SavingsAccount

Накопительный счёт, наследуется от `Account`. Списание разрешено, только если
после него баланс останется неотрицательным.

## CheckingAccount

Расчётный счёт, наследуется от `Account`.

* `__init__(self, owner: str, balance: float = 0, overdraft: float = 0)` —
  добавляет поле `overdraft`, предельная глубина ухода в минус;
* списание разрешено, если баланс после него не опустится ниже `-overdraft`.

## FixedDepositAccount

Срочный вклад, наследуется от `SavingsAccount`. Списание не разрешено никогда,
независимо от суммы и баланса. Пополнение работает как у всех.

## Примеры

```python
savings = SavingsAccount("Алиса", 100)
savings.withdraw(60)
savings.balance  # 40
savings.history  # ["-60"]
savings.withdraw(50)  # ValueError: не хватает средств

checking = CheckingAccount("Боб", 100, overdraft=500)
checking.withdraw(300)
checking.balance  # -200

deposit = FixedDepositAccount("Вера", 1000)
deposit.deposit(100)  # можно
deposit.withdraw(1)  # ValueError

Account("Гость").can_withdraw(1)  # NotImplementedError
Account.total_balance([savings, checking])  # -160
sorted([checking, savings])[0] is checking  # True, у него баланс меньше
```
