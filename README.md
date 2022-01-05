tqdm-thread
===========

When you want to show that something is working, but don't have an iterable. For example, if you're loading a large
Pickle file and want to show progress.

```python
import time
from tqdm_thread import tqdm_thread

with tqdm_thread(desc="doing serious work"):
    # do something that takes a long time
    time.sleep(3)

```

We also override the default `bar_format` since the tqdm default doesn't really make sense here. 


Tests
-----

```shell
# pip install pytest

pytest -vs .
```