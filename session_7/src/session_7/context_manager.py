import logging
import sys
import time
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time.perf_counter()
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
        self.end = time.perf_counter()
        logger.info(f"Execution time: {self.end-self.start}")
        return False


if __name__ == "__main__":
    with FileOpener("example.txt", "w") as f:
        f.write("Hello, Context Managers!"*1000000)





from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    print("\nUsing context Manager generator")
    print(f"Opening file{filename}")
    start = time.perf_counter()
    f = open(filename, mode)
    try:
        yield f
    finally:
        print(f"Closing file {filename}")
        f.close()
        end = time.perf_counter()
        logger.info(f"Execution time: {end-start}")
        
# Usage example:
if __name__ == "__main__":
    with open_file("example.txt", "a") as f:
        f.write("\nAppending with context manager using @contextmanager."*1000000)
