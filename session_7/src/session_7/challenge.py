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
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            print(f"File {self.filename} not fount")
        except AttributeError:
            print(f" {AttributeError}: type name Error ")
        finally:
            return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
        self.end = time.perf_counter()
        logger.info(f"Execution time: {self.end-self.start}")
        return False


if __name__ == "__main__":
    with FileOpener("1", "w") as f:
        f.write("Hello, Context Managers!"*1000000)





from contextlib import contextmanager
@contextmanager
def open_file(filename, mode):
    print("\nUsing context Manager generator")
    print(f"Opening file {filename}")
    start = time.perf_counter()
    try:
        f = open(filename, mode)
        yield f
    except FileNotFoundError:
        print(f" {filename} File not found")
    except ValueError:
        print(f" {ValueError}")
    except TypeError:
        print(f" {TypeError}")

    finally:
        print(f"Closing file {filename}")
        f.close()
        end = time.perf_counter()
        logger.info(f"Execution time: {end-start}")
        
if __name__ == "__main__":
        with open_file("example.txt", "a") as f:
            f.write("\nAppending with context manager using @contextmanager."*1000000)