from typing import (
    Union,)

def time_formatter(
    ms: Union[int, float]
) -> str:
    (
        minutes,
        seconds,
    ) = divmod(
        int(ms / 1000),
        60,
    )
    (
        hours,
        minutes,
    ) = divmod(minutes, 60)
    (
        days,
        hours,
    ) = divmod(hours, 24)
    (
        weeks,
        days,
    ) = divmod(days, 7)
    tmp = (
        (
            (str(weeks) + "w, ")
            if weeks
            else ""
        )
        + (
            (str(days) + "d, ")
            if days
            else ""
        )
        + (
            (str(hours) + "h, ")
            if hours
            else ""
        )
        + (
            (str(minutes) + "m, ")
            if minutes
            else ""
        )
        + (
            (str(seconds) + "s, ")
            if seconds
            else ""
        )
    )
    return tmp and tmp[:-2] or "0s"
