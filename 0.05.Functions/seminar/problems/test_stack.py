from stack import Stack


def test_new_stack_is_empty() -> None:
    stack = Stack()
    assert stack.size() == 0
    assert stack.is_empty() is True


def test_push_and_size() -> None:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.is_empty() is False


def test_pop_returns_the_last_pushed() -> None:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.size() == 0


def test_pop_on_an_empty_stack() -> None:
    assert Stack().pop() is None


def test_pop_empties_the_stack_completely() -> None:
    stack = Stack()
    stack.push(5)
    stack.pop()
    assert stack.is_empty() is True
    assert stack.pop() is None


def test_peek_does_not_remove() -> None:
    stack = Stack()
    stack.push(7)
    assert stack.peek() == 7
    assert stack.peek() == 7
    assert stack.size() == 1


def test_peek_on_an_empty_stack() -> None:
    assert Stack().peek() is None


def test_two_stacks_are_independent() -> None:
    # Список значений должен создаваться в __init__, иначе стопки общие.
    first = Stack()
    second = Stack()
    first.push(1)
    assert first.size() == 1
    assert second.size() == 0
    assert second.pop() is None


def test_zero_is_a_normal_value() -> None:
    # Ноль ложен, но это значение, а не признак пустоты.
    stack = Stack()
    stack.push(0)
    assert stack.is_empty() is False
    assert stack.peek() == 0
    assert stack.pop() == 0
