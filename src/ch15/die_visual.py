"""Visualise 2D Die rolling using plotly and pandas"""


import plotly.express as px
import pandas as pd
from pathlib import Path
from die import Die

BASE_DIR = Path(__file__).parent.parent.parent
OUTPUT_DIR = BASE_DIR / "outputs" / "die"
# parents arg to true to avoid throwing errors if "outputs" does not exist
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


def roll_die():
    """Generate a graph for a single D1 roll(s)"""
    
    die = Die()
    die_sides = range(1, die.sides+1)

    die_rolls = [die.roll() for _ in range(500)]
    die_frequencies = [die_rolls.count(side) for side in die_sides]

    die_fig = px.bar(x=die_sides, y=die_frequencies, title="One D6 Roll Results")
    die_fig.write_html(OUTPUT_DIR / "die_roll.html")


def roll_dice():
    """Generate a graph for dice roll(s) using pandas backend"""

    die_1 = Die(8)
    die_2 = Die(8)
    dice_results = range(2, (die_1.sides + die_2.sides)+1)

    dice_rolls = [(die_1.roll() + die_2.roll()) for _ in range(1000)]
    dice_frequency = []
    for result in dice_results:
        dice_frequency.append(dice_rolls.count(result))

    pd.options.plotting.backend = "plotly"
    df = pd.DataFrame({
        "result": dice_results,
        "frequency": dice_frequency
    })

    dice_fig = df.plot.bar(
        x="result",
        y="frequency",
        labels={"result":"Dice Result", "frequency":"Frequency of Result"}
    )
    dice_fig.write_html(OUTPUT_DIR / "dice_roll.html", auto_open=True)
    

if __name__ == "__main__":
    roll_die()
    roll_dice()