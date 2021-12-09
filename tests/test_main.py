import pytest
import json
import functools

from main import get_triplet_of_compatible_tracks


def pytest_configure():
    with open("data/songs.json", "r") as f:
        pytest.all_tracks = json.load(f)["all_tracks"]


@pytest.fixture
@functools.lru_cache
def data():
    with open("data/songs.json", "r") as f:
        return json.load(f)["all_tracks"]


def test_main_succeeds(data):
    # When concert_premiere_length matches a sum of duration of a triplet
    concert_premiere_length = 20
    tolerance = 5
    assert get_triplet_of_compatible_tracks(data, concert_premiere_length)
    assert get_triplet_of_compatible_tracks(data, concert_premiere_length, tolerance)

    concert_premiere_length = 1
    # When concert_premiere_length is too low but tolerance allows a match
    assert get_triplet_of_compatible_tracks(data, concert_premiere_length, tolerance)

    # When concert_premiere_length is too high low but tolerance allows a match
    concert_premiere_length = 25
    assert get_triplet_of_compatible_tracks(data, concert_premiere_length, tolerance)


def test_main_fails(data):
    # When concert_premiere_length doesn't match a sum of duration of a triplet
    concert_premiere_length = 1
    assert not get_triplet_of_compatible_tracks(data, concert_premiere_length)

    concert_premiere_length = 25
    assert not get_triplet_of_compatible_tracks(data, concert_premiere_length)

    concert_premiere_length = 1
    tolerance = 1
    # When concert_premiere_length is too low and tolerance not allows a match
    assert not get_triplet_of_compatible_tracks(data, concert_premiere_length, tolerance)

    # When concert_premiere_length is too high low and tolerance not allows a match
    concert_premiere_length = 25
    assert not get_triplet_of_compatible_tracks(data, concert_premiere_length, tolerance)