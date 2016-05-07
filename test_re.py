import pytest

from park import ReccomendEngine


@pytest.fixture(scope='session')
def rec_engine():
    r = ReccomendEngine()
    return r


def test_example_file_reccomendations_by_distance(rec_engine):
    rec_engine.handle_file()
    assert rec_engine.reccomend_by_distance() == [(3, 6, 0.6), (4, 7, 0.0), (0, 10, 0.8)]


def test_example_file_reccomendations_by_distance_pretty(rec_engine):
    rec_engine.handle_file()
    assert rec_engine.reccomend_by_distance(pretty=True) == [3, 4, 0]


def test_example_file_reccomendations_by_distance_and_rating(rec_engine):
    rec_engine.handle_file()
    assert rec_engine.reccomend_by_distance_ratings() == [(0, 10, 0.8), (3, 6, 0.6), (4, 7, 0.0)]


def test_example_file_reccomendations_by_distance_and_rating_pretty(rec_engine):
    rec_engine.handle_file()
    assert rec_engine.reccomend_by_distance_ratings(pretty=True) == [0, 3, 4]
