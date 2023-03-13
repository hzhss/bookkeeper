import pytest

from bookkeeper.models.budget import Budget


def test_create_with_full_args_list():
    b = Budget(period='День', limit=10, spent=5, pk=1)
    assert b.period == 'День'
    assert b.limit == 10
    assert b.spent == 5


def test_period_values():
    for period in ["День", "Неделя", "Месяц"]:
        b = Budget(period=period, limit=0, spent=0, pk=1)

    with pytest.raises(ValueError):
        b = Budget(period='20', limit=1, spent=3, pk=1)