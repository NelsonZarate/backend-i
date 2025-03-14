from typer import Typer
import logging
import sys
import time
from rich import print


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


app = Typer()

@app.command()
def square(num: int )-> int:
    logger.info("Command square started")
    command_square_start = time.perf_counter()
    print(f"input num: {num} square: {num * num}")
    command_square_end = time.perf_counter()
    logger.info("command square finished")
    logger.info(f"command square running time: {command_square_end-command_square_start:.8f}")
    return 


if __name__ == "__main__":
    logger.info("app started !!")
    app()

