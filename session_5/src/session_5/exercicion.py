import logging
import sys
from datetime import datetime 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


def log_calls(func):
    """A decorator that logs function call details."""
    def wrapper(*args, **kwargs):
        logger.info(f"start time: {datetime.now()} ")
        logger.info(f"Calling {func.__name__}() with args: {args}")
        # print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__}() returned: {result} ")
        logger.info(f"time ended: {datetime.now()}")
        #print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


@log_calls
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Result of add:", add(3, 4))
