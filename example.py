import time

from tqdm_thread import tqdm_thread


def main():
  with tqdm_thread(desc="speedy ..."):
    print("I'm fast")
    time.sleep(0.01)

  with tqdm_thread(desc="sleepy ..."):
    for _ in range(10):
      print(_)
      time.sleep(1)


if __name__ == '__main__':
  main()
