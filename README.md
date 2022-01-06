tqdm-thread
===========
[![Python application](https://github.com/riklopfer/tqdm-thread/actions/workflows/python-app.yml/badge.svg)](https://github.com/riklopfer/tqdm-thread/actions/workflows/python-app.yml)

When you want to show that something is working, but don't have an iterable. For example, if you're loading a large
Pickle file and want to show progress. All kwargs work as expected with tqdm with a couple exceptions:

1. `step_sec` -- this is new. how many seconds to sleep between steps. default: `1.0`
1. `total` -- since we don't actually know the total, this create a new progress bar every `total` steps. default: `None`
1. default `bar_format` is different; if `total` then '{desc} {bar} {elapsed}' else '{desc} {elapsed}'

```python
import time
from tqdm_thread import tqdm_thread

with tqdm_thread(desc="doing serious work"):
    # do something that takes a long time
    time.sleep(10)

with tqdm_thread(desc="doing serious work", total=20):
    # do something that takes a long time
    time.sleep(10)

with tqdm_thread(desc="doing serious work", total=10, step_sec=1):
    # do something that takes a long time
    time.sleep(10)


```


Tests
-----

```shell
# pip install pytest

pytest -vs .
```
