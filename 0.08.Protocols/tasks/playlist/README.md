# playlist

Питон почти нигде не спрашивает, какого класса объект. Он спрашивает, что
объект **умеет**: цикл `for` не проверяет, список ему дали или кортеж, — он
пробует получить элементы. Набор методов, которого достаточно, чтобы объект
где-то заработал, и называют протоколом; в коде он нигде не записан.

Плейлисту хватит двух методов, чтобы вести себя как список: по нему пойдёт
`for`, заработают `in`, `reversed`, распаковка, `sorted`. Механика такая: если
у объекта нет `__iter__`, `for` дёргает `__getitem__` с числами 0, 1, 2 и так
далее, пока не получит `IndexError`. Отсюда следствие: **`IndexError` за
границей обязателен**, иначе любой `for` по плейлисту станет вечным.

## Что реализовать

Класс `Playlist` — список треков.

* `__init__(self, tracks: list[str])` — список нужно скопировать, иначе
  плейлист будет меняться вслед за исходным;
* `__len__`;
* `__getitem__` — по целому числу трек, по срезу **новый `Playlist`**, а не
  список: иначе от результата среза уже нельзя будет взять срез. Срез приходит
  одним аргументом — объектом `slice`, а не двумя числами. Отрицательные
  номера работают как у списка, выход за границы даёт `IndexError`;
* `__repr__` — `Playlist(['a', 'b'])`;
* `can_iterate(value: Any) -> bool` — статический метод: перебирается ли
  объект. Отвечать нужно попыткой — позвать `iter` и поймать `TypeError`.

Спросить то же самое через `isinstance(value, abc.Iterable)` не выйдет: он
смотрит на наличие `__iter__`, а его у плейлиста нет. Про старый путь перебора
не знает и `mypy`, поэтому в тестах плейлисты помечены как `Any`.

## Примеры

```python
playlist = Playlist(["Intro", "Verse", "Chorus", "Outro"])

playlist[0]  # "Intro"
playlist[-1]  # "Outro"
playlist[1:3]  # Playlist(['Verse', 'Chorus'])
playlist[1:3][0]  # "Verse"
playlist[::-1]  # Playlist(['Outro', 'Chorus', 'Verse', 'Intro'])
playlist[10]  # IndexError

len(playlist)  # 4
"Chorus" in playlist  # True — не писали, а работает
list(reversed(playlist))  # ["Outro", "Chorus", "Verse", "Intro"]
sorted(playlist)  # ["Chorus", "Intro", "Outro", "Verse"]

isinstance(playlist, abc.Iterable)  # False — а list(playlist) работает

Playlist.can_iterate(playlist)  # True
Playlist.can_iterate("строка")  # True
Playlist.can_iterate(42)  # False
```
