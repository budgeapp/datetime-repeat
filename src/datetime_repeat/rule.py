from dataclasses import dataclass
from datetime import date, datetime
from typing import Set

from datetime_repeat.types import (
    Frequency,
    Month,
    Weekday,
)


@dataclass(frozen=True)
class RepeatRule:
    frequency: Frequency
    interval: int = 1
    start_date: date | None = None
    end_date: date | None = None
    count: int | None = None
    weekdays: Weekday | Set[Weekday] | None = None
    months: Month | Set[Month] | None = None
    monthdays: int | Set[int] | None = None
    yeardays: int | Set[int] | None = None

    @property
    def _start_date(self) -> date:
        return self.start_date or (
            date.today() if self.frequency >= Frequency.DAILY else datetime.now()
        )
