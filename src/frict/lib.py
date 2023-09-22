import sys
from typing import Any
import typing


def frict(
    *obj: Any,
    sep: str = '',
    end: str = '\n',
    file: typing.IO[str] = sys.stdout,
    flush: bool = False,
):
    print(*obj, sep=sep, end=end, file=file, flush=flush)
