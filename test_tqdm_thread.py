# import pytest

import time

from tqdm_thread import tqdm_thread


def test_short():
    print("I'm fast")
    with tqdm_thread(desc="speedy ..."):
        time.sleep(0.01)


def test_no_desc():
    with tqdm_thread():
        time.sleep(1)


def test_longer():
    print("I'm slow(ish)")
    with tqdm_thread(desc="sleepy ..."):
        time.sleep(3)


def test_longest():
    print("I'm slooowwwww")
    with tqdm_thread(desc="super sleepy ...", total=10):
        time.sleep(30)
