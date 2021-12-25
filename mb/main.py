import itertools
import time
import argparse

art = [r"""
/         O    \
|  O . O   .   |
\           O  /
""",r"""
/     O    O   \
|    .     .   |
\   O      O   /
""",r"""
/    O      O  \
|    .     .   |
\    O    O    /
""",r"""
/   O          \
|    .   O . O |
\     O        /
""",
]

def main():
    parser = argparse.ArgumentParser(
        prog="mb",
        description='Use advanced impulse techniques to soothe and de-stress your terminal.')
    parser.add_argument('--warm',
                        action="store_true",
                        help='Provide warming impulses to the terminal')
    parser.add_argument('--speed', choices=["slow", "normal", "fast"],
                        default="normal",
                        help='Speed of provision of impulses')
    args = parser.parse_args()

    first = True
    for frame in itertools.cycle(art):
        if args.warm:
            frame = frame.replace('O', '\033[0;30;41mO\033[0;0m')
        if first:
            first = False
        else:
            print("\033[5A\r\033[J", end="")
        print(frame)
        if args.speed == "slow":
            time.sleep(0.3)
        elif args.speed == "fast":
            time.sleep(0.075)
        else:
            time.sleep(0.15)


if __name__ == "__main__":
    main()
