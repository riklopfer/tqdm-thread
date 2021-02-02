tqdm-thread
===========

When you want to show that something is working, but don't have an iterable. For example, if you're
loading a large Pickle file and want to show progress.

```python
from tqdm_thread import tqdm_thread

with tqdm_thread(desc="doing serious work"):
  # do something that takes a long time
  pass

```