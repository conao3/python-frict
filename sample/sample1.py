import argparse
import inspect
import math
import random
import sys
import time

import frict


def main_1(args: argparse.Namespace) -> None:
    print('hello')


def main_2(args: argparse.Namespace) -> None:
    with frict.frict() as frict_:
        frict_('hello')
        time.sleep(1)
        frict_('world')


def main_3(args: argparse.Namespace) -> None:
    strings = [
        '''\
1
2
3''',
        '''\
4
5''',
        '''\
6
7
8''',
        '''\
9''',
    ]
    with frict.frict() as frict_:
        for string in strings:
            frict_(string)
            time.sleep(1)


def main_4(args: argparse.Namespace) -> None:
    signs = ['|', '/', '-', '\\']
    with frict.frict() as frict_:
        for inx in range(30):
            frict_(signs[inx % len(signs)])
            time.sleep(0.1)


def main_5(args: argparse.Namespace) -> None:
    signs = ['|', '/', '-', '\\']
    total_frames = 50
    with frict.frict() as frict_:
        counter = 12532
        for inx in range(total_frames):
            sign = signs[inx % len(signs)]
            angle = (inx / total_frames) * 4 * math.pi
            pos1 = int(math.sin(angle) * 15) + 15
            pos2 = int(math.sin(angle + 90) * 15) + 15
            if random.random() < 0.7:
                counter += int(random.random() * 500)
            target = f'''\
      {'*':>{pos1}}
   {sign} Welcome my homepage! {sign}
      {sign} You are visitor number: {counter} {sign}
      {'*':>{pos2}}'''
            frict_(target)
            time.sleep(0.1)


def list_main_functions() -> list[str]:
    fns = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    return list(elm[0] for elm in fns if elm[0].startswith('main_'))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('main', choices=list_main_functions())
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    getattr(sys.modules[__name__], args.main)(args)


main()
