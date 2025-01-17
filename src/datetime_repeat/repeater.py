from dataclasses import dataclass, field
from datetime import date
from typing import Set

from datetime_repeat.rule import RepeatRule


@dataclass
class Repeater:
    rrules: Set[RepeatRule] = field(default_factory=set)
    rdates: Set[date] = field(default_factory=set)
    exrules: Set[RepeatRule] = field(default_factory=set)
    exdates: Set[date] = field(default_factory=set)
