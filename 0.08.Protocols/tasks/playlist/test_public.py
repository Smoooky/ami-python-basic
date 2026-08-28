from typing import Any

import pytest
from playlist import Playlist

TRACKS = ["Intro", "Verse", "Chorus", "Outro"]

# Плейлисты в тестах помечены как Any намеренно: mypy не знает про старый
# протокол перебора через __getitem__ и ругался бы на list(playlist) и
# "Chorus" in playlist, хотя во время выполнения это работает.


def test_length_and_indexing() -> None:
    playlist: Any = Playlist(TRACKS)
    assert len(playlist) == 4
    assert playlist[0] == "Intro"
    assert playlist[-1] == "Outro"
    with pytest.raises(IndexError):
        _ = playlist[10]


def test_slice_gives_another_playlist() -> None:
    playlist: Any = Playlist(TRACKS)
    part = playlist[1:3]
    assert list(part) == ["Verse", "Chorus"]
    assert part[0] == "Verse"
    assert isinstance(part, Playlist)


def test_iteration_comes_for_free() -> None:
    playlist: Any = Playlist(TRACKS)
    assert list(playlist) == TRACKS
    assert "Chorus" in playlist
    assert "Bridge" not in playlist
    assert list(reversed(playlist)) == ["Outro", "Chorus", "Verse", "Intro"]
    assert sorted(playlist) == ["Chorus", "Intro", "Outro", "Verse"]


def test_can_iterate() -> None:
    assert Playlist.can_iterate(Playlist(TRACKS)) is True
    assert Playlist.can_iterate([1, 2]) is True
    assert Playlist.can_iterate("строка") is True
    assert Playlist.can_iterate(42) is False
