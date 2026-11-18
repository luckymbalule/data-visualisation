import json
import pandas as pd
from pandas import Series
import plotly.express as px
from pathlib import Path
from typing import NamedTuple


BASE_DIR = Path(__file__).parent.parent.parent
OUTPUT_DIR = BASE_DIR / "outputs" / "map"
RAW_PATH = BASE_DIR / "data" / "earthquake.geojson"
FORMAT_PATH = BASE_DIR / "data" / "formatted" / "eq_data.geojson"

FORMAT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


class PlotProp(NamedTuple):
    df: list | pd.DataFrame
    sizes: list[float] | Series
    title: str


def load_py():
    with open(RAW_PATH, encoding="utf-8") as rf:
        raw_data = json.load(rf)

    # Testing a write
    with open(FORMAT_PATH, mode="w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=4)

    rows = [
        {
            "mag": data["properties"]["mag"],
            "lon": data["geometry"]["coordinates"][0],
            "lat": data["geometry"]["coordinates"][1],
        }
        for data in raw_data["features"]
        if data["properties"]["mag"] is not None
        and data["properties"]["mag"] >= 0
    ]
    plot_sizes = [2 ** x["mag"] for x in rows]

    return PlotProp(df=rows, sizes=plot_sizes,
                    title=raw_data["metadata"]["title"]
                    )


def load_pandas():
    with open(RAW_PATH, encoding="utf-8") as f:
        json_data = json.load(f)

    rows = [
        {
            "mag": jd["properties"]["mag"],
            "lon": jd["geometry"]["coordinates"][0],
            "lat": jd["geometry"]["coordinates"][1],
        }
        for jd in json_data["features"]
    ]

    df = pd.DataFrame(rows)

    # Filter significant quakes/magnitudes - using M 0 as the base
    significant_df = df[df["mag"] >= 0]
    plot_sizes = 2 ** significant_df["mag"]

    return PlotProp(df=significant_df, sizes=plot_sizes,
                    title=json_data["metadata"]["title"]
                    )


def plot_eq():
    # Load data
    # spec = load_py()
    spec = load_pandas()

    fig = px.scatter_geo(spec.df, lon="lon", lat="lat",
                            size=spec.sizes,
                            size_max=50,
                            custom_data=["mag", "lon", "lat"],
                            title=spec.title
                        )
    fig.update_traces(hovertemplate = 
                        "Magnitude: %{customdata[0]}<br>" +
                        "Longitude: %{customdata[1]}<br>" +
                        "Latitude: %{customdata[2]}"
                    )
    fig.write_html(OUTPUT_DIR / "eq_2025.html", auto_open=True)


if __name__ == "__main__":
    plot_eq()