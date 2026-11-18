import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

from weather_loader import WeatherColumn, load_py_weather, load_pandas_weather


BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / "data"

ZOMBA_DATA = DATA_DIR / "zomba_weather_2025.csv"
NTCHEU_DATA = DATA_DIR / "ntcheu_weather_2025.csv"


def plot_py_weather():
    """Plot the standard python derived data"""

    datasets = {
        "zomba": load_py_weather(ZOMBA_DATA),
        "ntcheu": load_py_weather(NTCHEU_DATA)
    }

    fig, axs = plt.subplots(
        2, sharex=True, sharey=True, layout="constrained"
    )

    for ax, (location, dt) in zip(axs, datasets.items()):
        ax.set_title(location.upper())
        ax.set_ylabel("Temperature (°C)")
        ax.plot(
            dt[WeatherColumn.DATE.value],
            dt[WeatherColumn.T_MAX.value],
            color="red"
        )
        ax.plot(
            dt[WeatherColumn.DATE.value],
            dt[WeatherColumn.T_MIN.value],
            color="blue"
        )
        ax.fill_between(
            dt[WeatherColumn.DATE.value],
            dt[WeatherColumn.T_MAX.value],
            dt[WeatherColumn.T_MIN.value],
            color="blue",
            alpha=0.1
        )
    fig.suptitle("Temperature Comparison", fontsize=16)
    fig.autofmt_xdate()
    plt.show()


def plot_pandas_weather(dataframes: dict, title="Rainfall Comparison"):
    """Visualise from pandas dataframe"""

    dataframe = pd.concat(dataframes)
    df = dataframe[WeatherColumn.PRECIP.value].unstack(level=0)
    df = df.resample("ME").sum()
    df.index = df.index.strftime("%b")

    plt.close("all")
    ax = df.plot.bar(
        title=title,
        rot=0
    )
    ax.set_ylabel("Precipitation (mm)")
    plt.show()


if __name__ == "__main__":
    weather_data = {
        "ntcheu": load_pandas_weather(NTCHEU_DATA),
        "zomba": load_pandas_weather(ZOMBA_DATA)
    }

    plot_pandas_weather(weather_data)
    plot_py_weather()