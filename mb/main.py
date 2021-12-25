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

big_art = [
r"""
//                        \\
||   /\          /\       ||
||   \/          \/       ||
||      .           .     ||
||        /\          /\  ||
||        \/          \/  ||
\\                        //
""",
r"""
//                        \\
||               /\       ||
||   /\          \/       ||
||   \/ . /\        .     ||
||        \/          /\  ||
||                    \/  ||
\\                        //
""",
r"""
//                        \\
||               /\       ||
||        /\     \/       ||
||   /\ . \/        .     ||
||   \/               /\  ||
||                    \/  ||
\\                        //
""",
r"""
//                        \\
||        /\     /\       ||
||        \/     \/       ||
||      .           .     ||
||   /\               /\  ||
||   \/               \/  ||
\\                        //
""",
r"""
//                        \\
||       /\      /\       ||
||       \/      \/       ||
||      .           .     ||
||    /\              /\  ||
||    \/              \/  ||
\\                        //
""",
r"""
//                        \\
||      /\       /\       ||
||      \/       \/       ||
||      .           .     ||
||     /\             /\  ||
||     \/             \/  ||
\\                        //
""",
r"""
//                        \\
||     /\        /\       ||
||     \/        \/       ||
||      .           .     ||
||      /\            /\  ||
||      \/            \/  ||
\\                        //
""",
r"""
//                        \\
||    /\         /\       ||
||    \/         \/       ||
||      .           .     ||
||       /\           /\  ||
||       \/           \/  ||
\\                        //
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
                        help='Speed of impulses')
    parser.add_argument('--big',
                        action="store_true",
                        help="Be big")
    args = parser.parse_args()

    first = True
    if args.big:
        frames = big_art
        sphere = ["/\\", '\\/']
    else:
        frames = art
        sphere = ["O"]
    for frame in itertools.cycle(frames):
        if args.warm:
            for elem in sphere:
                frame = frame.replace(elem, '\033[0;30;41m' + elem + '\033[0;0m')
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
