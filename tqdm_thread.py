from threading import Thread, Event

from tqdm import tqdm


class _TQDM(Thread):
    def __init__(self, sleep, **kwargs):
        super(_TQDM, self).__init__()
        self.sleep = sleep
        self._is_dead = Event()
        self._tqdm_kwargs = kwargs
        
        # override default bar_format
        if 'bar_format' not in self._tqdm_kwargs:
            self._tqdm_kwargs = {
                'bar_format': '{desc} {elapsed}',
                **kwargs
            }

    def _generator(self):
        while not self._is_dead.is_set():
            yield None

    def run(self) -> None:
        for _ in tqdm(self._generator(), **self._tqdm_kwargs):
            self._is_dead.wait(self.sleep)

    def stop(self):
        self._is_dead.set()


class tqdm_thread(object):
    def __init__(self, sleep=0.1, **kwargs):
        """
        :param sleep: number of seconds to sleep between tqdm iterations
        :param kwargs: kwargs passed along to tqdm
        """
        self._thread = _TQDM(sleep, **kwargs)

    def __enter__(self):
        self._thread.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._thread.stop()
