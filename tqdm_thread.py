import time
from threading import Thread, Event

from tqdm import tqdm


class _TQDM(Thread):
  def __init__(self, sleep, **kwargs):
    super(_TQDM, self).__init__()
    self.sleep = sleep
    self._is_dead = Event()
    self._tqdm_kwargs = kwargs

  def _generator(self):
    while not self._is_dead.isSet():
      yield None

  def run(self) -> None:
    for _ in tqdm(self._generator(), **self._tqdm_kwargs):
      time.sleep(self.sleep)

  def stop(self):
    self._is_dead.set()


class tqdm_thread(object):
  def __init__(self, sleep=.1,
      desc='tqdm thread',
      bar_format='{desc} {elapsed}',
      **kwargs):
    """
    :param sleep: the amount of time to sleep between tqdm iterations
    :param kwargs: kwargs passed along to tqdm constructor
    """
    self._thread = _TQDM(sleep, desc=desc, bar_format=bar_format, **kwargs)

  def __enter__(self):
    self._thread.start()

  def __exit__(self, exc_type, exc_val, exc_tb):
    self._thread.stop()
