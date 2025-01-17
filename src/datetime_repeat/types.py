from enum import Enum, IntEnum

from dateutil.rrule import FR, MO, SA, SU, TH, TU, WE


class Frequency(IntEnum):
    SECONDLY = 0
    MINUTELY = 1
    HOURLY = 2
    DAILY = 3
    WEEKLY = 4
    MONTHLY = 5
    YEARLY = 6


class Month(IntEnum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class Weekday(Enum):
    MON = MO
    TUE = TU
    WED = WE
    THU = TH
    FRI = FR
    SAT = SA
    SUN = SU
