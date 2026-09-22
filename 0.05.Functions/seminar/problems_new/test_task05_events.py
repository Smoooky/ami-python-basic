from task05_events import Emitter


def test_emit_unknown_event_returns_zero() -> None:
    em = Emitter()
    assert em.emit("click") == 0


def test_on_then_emit_returns_count() -> None:
    em = Emitter()
    calls = []
    em.on("click", lambda *a: None)
    em.on("click", lambda *a: calls.append(a))
    assert em.emit("click", 1, 2) == 2
    assert calls == [(1, 2)]


def test_handlers_run_in_subscription_order() -> None:
    em = Emitter()
    order = []
    em.on("тик", lambda *a: order.append(1))
    em.on("тик", lambda *a: order.append(2))
    em.on("тик", lambda *a: order.append(3))
    em.emit("тик")
    assert order == [1, 2, 3]


def test_duplicate_subscription_is_ignored() -> None:
    em = Emitter()
    calls = []

    def handler(*args):
        calls.append(args)

    em.on("e", handler)
    em.on("e", handler)
    assert em.emit("e") == 1
    assert calls == [()]


def test_events_are_independent() -> None:
    em = Emitter()
    log = []
    em.on("a", lambda *x: log.append("a"))
    em.on("b", lambda *x: log.append("b"))
    assert em.emit("a") == 1
    assert log == ["a"]


def test_off_removes_subscription() -> None:
    em = Emitter()
    calls = []

    def handler(*args):
        calls.append(args)

    em.on("e", handler)
    assert em.off("e", handler) is True
    assert em.off("e", handler) is False
    assert em.emit("e") == 0
    assert calls == []


def test_off_unknown_event_returns_false() -> None:
    em = Emitter()
    assert em.off("нет такого", lambda *a: None) is False


def test_bound_methods_of_different_objects_are_distinct() -> None:
    class Counter:
        def __init__(self):
            self.hits = 0

        def hit(self, *args):
            self.hits += 1

    em = Emitter()
    first, second = Counter(), Counter()
    em.on("tick", first.hit)
    em.on("tick", second.hit)
    assert em.emit("tick") == 2
    assert first.hits == 1 and second.hits == 1
    # Главная проверка: отписка метода одного объекта не трогает другой.
    assert em.off("tick", first.hit) is True
    assert em.emit("tick") == 1
    assert first.hits == 1 and second.hits == 2


def test_once_fires_single_time() -> None:
    em = Emitter()
    calls = []
    em.once("бум", lambda *a: calls.append(a))
    assert em.emit("бум", 7) == 1
    assert em.emit("бум", 7) == 0
    assert calls == [(7,)]


def test_once_does_not_touch_regular_handlers() -> None:
    em = Emitter()
    calls = []
    em.once("e", lambda *a: calls.append("один раз"))
    em.on("e", lambda *a: calls.append("всегда"))
    em.emit("e")
    em.emit("e")
    # Главная проверка: обёртка сняла только себя, обычная подписка жива.
    assert calls == ["один раз", "всегда", "всегда"]
