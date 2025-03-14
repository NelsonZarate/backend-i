from typer import Typer
import logging
import sys
import time
from session_9.bot import run


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


app = Typer()

@app.command()
def runbot():
    logger.info("Command runBot started")
    command_run_bot_start = time.perf_counter()
    run()
    command_run_bot_end = time.perf_counter()
    logger.info("command runBot finished")
    logger.info(f"command runBot running time: {command_run_bot_end-command_run_bot_start:.8f}")
    return 

@app.command()
def bot():
    return

if __name__ == "__main__":
    logger.info("app started !!")
    app()

