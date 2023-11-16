import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

@cmd_group.command()
@click.argument("accuracy")
@click.option(
    "-d",
    "--decimals",
    default=3,
)
def approx(accuracy, decimals):
    x = 0
    accuracy = float(accuracy)
    while x < 2 * np.pi:
        if np.abs(x - np.sin(x)) > accuracy:
            print((f"For an accuracy of {float(accuracy)}, the small-angle"
                    f" approximation holds up to x = {round(x, decimals)}."))
            return
        x += 10 ** -(decimals)
    return

if __name__ == "__main__":
    cmd_group()
