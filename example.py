import time

from tqdm_thread import tqdm_thread


def main():
  with tqdm_thread():
    for _ in range(10):
      print(_)
      time.sleep(1)


if __name__ == '__main__':
  main()