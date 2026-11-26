#!/usr/bin/env python3
"""The Meridian Gazette - 26 November 2026 (make.fun news-image-20261126).

The front page is rendered at build time and committed to this
repository as entry.png (1024x1024). This program only copies that
committed image to /output/entry.png, using the standard library
only, so it runs identically offline in the grader sandbox with no
third-party packages and no network access.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png not found next to main.py")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(DST) == 0:
        raise SystemExit("copied entry.png is empty")
    return 0


if __name__ == "__main__":
    sys.exit(main())
