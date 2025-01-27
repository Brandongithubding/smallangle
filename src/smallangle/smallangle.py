import click
import numpy as np
from numpy import pi
import pandas as pd

# Create the small-angle group for the subcommands.
@click.group()
def cmd_group():
    pass

# Sin command.
@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="The number of values used from the interval."
)
def sin(number):
    """Gives values of sin for "number" values equally seperated in [0, 2pi].

    Side Effects:
        Prints the sin(x) values next to the x values from the interval.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

# Tan command.
@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="The number of values used from the interval."
)
def tan(number):
    """Gives values of tan for "number" values equally seperated in [0, 2pi].

    Side Effects:
        Prints the tan(x) values next to the x values from the interval.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

# Small-angle approximation command.
@cmd_group.command()
@click.argument("accuracy")
@click.option(
    "-d",
    "--decimals",
    default=3,
    help="The decimal precision that is used to approximate."
)
def approx(accuracy, decimals):
    """Gives the highest angle so that the small-angle inequality holds. This is
    the highest angle for which x can be used instead of sin(x) while still
    keeping the wanted amount of accuracy.

    Args:
        accuracy (float): The accuracy used in the small-angle inequality.

    Side Effects:
        Prints the small-angle approximation.
    """
    x = 0
    accuracy = float(accuracy)
    # Keep increasing until the inequality no longer holds.
    while x < 2 * np.pi:
        if np.abs(x - np.sin(x)) > accuracy:
            print((f"For an accuracy of {float(accuracy)}, the small-angle"
                    f" approximation holds up to x = {round(x, decimals)}."))
            return
        # Take the decimal option as the precision.
        x += 10 ** -(decimals)
    return

if __name__ == "__main__":
    cmd_group()
