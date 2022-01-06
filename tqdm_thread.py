from threading import Thread, Event

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
