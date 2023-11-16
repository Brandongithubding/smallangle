import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-a",
    "--amount",
    default=10,
)
def sin(amount):
    x = np.linspace(0, 2 * pi, amount)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@cmd_group.command()
@click.option(
    "-a",
    "--amount",
    default=10,
)
def tan(amount):
    x = np.linspace(0, 2 * pi, amount)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()