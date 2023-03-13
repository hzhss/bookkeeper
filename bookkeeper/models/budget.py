"""
Модель бюджета
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Budget:
    """
    Класс Бюджет за День, Неделю, Месяц.
    Выводит сколько было потрачено и лимит на покупки.
    """
    period: str
    limit: float = 0
    spent: float = 0
    pk: int = 0

    def __init__(self, period: str, limit: float = 0,
                 spent: float = 0, pk: int = 0):

        if period not in ["День", "Неделя", "Месяц"]:
            raise ValueError(f'unsupported value of period <{period}>')
        self.period = period
        self.limit = limit
        self.spent = spent
        self.pk = pk