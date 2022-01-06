import argparse
import subprocess
import sys
from threading import Thread, Event
from typing import List

from tqdm import tqdm


class _TQDM(Thread):
    def __init__(self, sleep, **kwargs):
        super(_TQDM, self).__init__()
        self.sleep = sleep
        self._is_done = Event()

        # special defaults
        default_kwargs = {}
        if 'total' in kwargs:
            default_kwargs['bar_format'] = '{desc} {bar} {elapsed}'
        else:
            default_kwargs['bar_format'] = '{desc} {elapsed}'

        default_kwargs.update(kwargs)

        self._kwargs = default_kwargs

    def _generator(self):
        steps_per_bar = self._kwargs.get('total', 0)
        if steps_per_bar:
            for _ in range(steps_per_bar):
                if self._is_done.is_set():
                    return
                yield None
        else:
            while not self._is_done.is_set():
                yield None

    def _new_tqdm(self):
        return tqdm(self._generator(), **self._kwargs)

    def run(self) -> None:
        while not self._is_done.is_set():
            for _ in self._new_tqdm():
                self._is_done.wait(self.sleep)

    def stop(self):
        self._is_done.set()


class tqdm_thread(object):
    def __init__(self, step_sec=1, **kwargs):
        """
        :param step_sec: number of seconds to sleep between steps
        :param kwargs: kwargs passed along to tqdm
        """
        self._thread = _TQDM(step_sec, **kwargs)

    def __enter__(self):
        self._thread.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._thread.stop()


def _exec_cmd(command_args: List[str], total: int, step_sec: int):
    assert cmd
    assert total >= 0
    assert step_sec > 0.1

    with tqdm_thread(step_sec=step_sec, total=total, desc=command_args[0]):
        try:
            subprocess.check_call(command_args)
        except Exception:
            return 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tqdm_total', help='', type=int, default=0)
    parser.add_argument('--tqdm_step_sec', help='', type=int, default=1)
    args, cmd = parser.parse_known_args()

    sys.exit(_exec_cmd(cmd, args.tqdm_total, args.tqdm_step_sec))
