# python-frict

Clear the previous output and produce a new one.

![capture](https://github.com/conao3/python-frict/assets/4703128/4a2566c0-0e22-460d-a75a-8891d155b71b)

# Usage

This example shows spinner.

```python
import frict

def main_4(args: argparse.Namespace) -> None:
    signs = ['|', '/', '-', '\\']
    with frict.frict() as frict_:
        for inx in range(30):
            frict_(signs[inx % len(signs)])
            time.sleep(0.1)
```

More funcy one.

```python
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
```
