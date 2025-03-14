import logging
import sys
from datetime import datetime
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


def check_user(func):
    """A decorator that logs function call details."""
    def wrapper(*args, **kwargs):
        logger.info(f"\nstart time: {datetime.now()} ")
        logger.info(f"Calling {func.__name__}() with args: {args}")
        username, password = args[0], args[1]
        if username in users:
            if password == users[username]:
                logger.info("Sucessfully logged in!")
                return logger.info(f"time ended: {datetime.now()} \n")
            print(f"password invalid")
            logger.error(f"{func.__name__}() returned: ERROR!! ")
            return
        else:
            result = func(*args, **kwargs)
            logger.info("user added and Sucessfully logged in!")
            logger.info(f"{func.__name__}() returned: {result} ")

        logger.info(f"time ended: {datetime.now()} \n")
        return result
    return wrapper


users = {}


@check_user
def add_users(user, password):
    users[user] = password
    return users


if __name__ == "__main__":
    add_users("Nelson", "12345")
    add_users("Nelson", "12345")
    add_users("Nelson", "jhsdjk")
