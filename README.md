tqdm-thread
===========

When you want to show that something is working, but don't have an iterable. For example, if you're loading a large
Pickle file and want to show progress.

```python
from tqdm_thread import tqdm_thread

with tqdm_thread(desc="doing serious work", sleep=0.1):
    # do something that takes a long time
    pass

```

**Note** It is possible that you will have to wait an unnecessary `sleep` seconds when using this. Usually this is okay
when `sleep` is a low value like the default value `0.1`. 

