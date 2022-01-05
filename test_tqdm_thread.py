# import pytest

import time

from tqdm_thread import tqdm_thread


def test_short():
    with tqdm_thread(desc="speedy ..."):
        print("I'm fast")
        time.sleep(0.01)


def test_no_desc():
    with tqdm_thread():
        time.sleep(0.01)


def test_longer():
    with tqdm_thread(desc="sleepy ..."):
        print("I'm slow(ish)")
        time.sleep(3)


def test_longest():
    with tqdm_thread(desc="super sleepy ..."):
        print("I'm slooowwwww")
        time.sleep(30)
