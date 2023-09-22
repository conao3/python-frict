import sys
from typing import Any
import typing


previous_lines = 0

def frict(
    *obj: Any,
    sep: str = '',
    end: str = '\n',
    file: typing.IO[str] = sys.stdout,
    flush: bool = False,
):
    global previous_lines

    if previous_lines:
        print(f'\033[{previous_lines}A\033[J', end='', file=file, flush=True)

    previous_lines = sum((str(elm) + end).count('\n') for elm in obj)
    print(*obj, sep=sep, end=end, file=file, flush=flush)
