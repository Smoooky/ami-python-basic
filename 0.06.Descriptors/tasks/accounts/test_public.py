import pytest
from accounts import CheckingAccount, FixedDepositAccount, SavingsAccount


def test_savings_cannot_go_negative() -> None:
    account = SavingsAccount("Алиса", 100)
    account.withdraw(60)
    assert account.balance == 40
    with pytest.raises(ValueError):
        account.withdraw(50)


def test_checking_allows_overdraft() -> None:
    account = CheckingAccount("Боб", 100, overdraft=500)
    account.withdraw(300)
    assert account.balance == -200


def test_fixed_deposit_forbids_withdrawal() -> None:
    account = FixedDepositAccount("Вера", 1000)
    account.deposit(100)
    assert account.balance == 1100
    with pytest.raises(ValueError):
        account.withdraw(1)
