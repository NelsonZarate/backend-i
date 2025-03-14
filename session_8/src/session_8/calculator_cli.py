from typer import Typer
import logging
import sys
import time
from rich import print
from typing_extensions import Annotated

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


app = Typer()

@app.command(help="Square of one number")
def square(num: int )-> int:
    logger.info("Command square started")
    command_square_start = time.perf_counter()
    print(f"input num: {num} square: {num * num}")
    command_square_end = time.perf_counter()
    logger.info("command square finished")
    logger.info(f"command square running time: {command_square_end-command_square_start:.8f}")
    return 

@app.command(help="sum of 2 numbers")
def addition(numbers: Annotated[list[int], Option(help="APP Calculator")]= []):
    logger.info("Command sum started")
    command_sum_start = time.perf_counter()
    result = sum(numbers)
    print(f"addition of the numbers {numbers} result of the sum:{result}")
    command_sum_end = time.perf_counter()
    logger.info("command sum finished")
    logger.info(f"command sum running time: {command_sum_end-command_sum_start:.8f}")
    return 

@app.command(help="subatraction of 2 numbers")
def substraction(num1:int,num2:int)->int:
    logger.info("Command subtraction started")
    command_subtraction_start = time.perf_counter()
    result = sum(num1,num2)
    print(f"input num: {num1} num2: {num2} result of the sum:{result}")
    command_substraction_end = time.perf_counter()
    logger.info("command sum finished")
    logger.info(f"command sum running time: {command_substraction_end-command_subtraction_start:.8f}")
    return 
    
if __name__ == "__main__":
    logger.info("app started !!")
    app()

