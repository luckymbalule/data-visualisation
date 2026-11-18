import csv
from pathlib import Path
from enum import StrEnum
from datetime import datetime
import pandas as pd


BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / "data"

ZOMBA_DATA = DATA_DIR / "zomba_weather_2025.csv"
NTCHEU_DATA = DATA_DIR / "ntcheu_weather_2025.csv"


class WeatherColumn(StrEnum):
    DATE = "time"
    T_MAX = "temperature_2m_max (°C)"
    T_MIN = "temperature_2m_min (°C)"
    SUNRISE = "sunrise (iso8601)"
    SUNSET = "sunset (iso8601)"
    PRECIP = "precipitation_sum (mm)"


def load_py_weather(data_file: Path):
    """Parse weather data using standard python loops"""
    try:
        row_num = None
        header_row = None
        weather_data = {
            WeatherColumn.DATE.value: [],
            WeatherColumn.T_MAX.value: [],
            WeatherColumn.T_MIN.value: [],
            WeatherColumn.PRECIP.value: [],
        }

        # Loading to memory - alternative
        # content = ZOMBA_DATA.read_text(encoding="utf-8").splitlines()

        with open(data_file, encoding="utf-8") as content:
            reader = csv.reader(content)
            line_number, header_row = _find_header(reader)

            date_index = header_row.index(WeatherColumn.DATE.value)
            t_max_index = header_row.index(WeatherColumn.T_MAX.value)
            t_min_index = header_row.index(WeatherColumn.T_MIN.value)
            precip_index = header_row.index(WeatherColumn.PRECIP.value)

            for row_num, row in enumerate(reader, start=line_number+2):
                current_date = datetime.strptime(
                    row[date_index], "%Y-%m-%d"
                )
                weather_data[WeatherColumn.DATE.value].append(current_date)
                weather_data[WeatherColumn.T_MAX.value].append(float(row[t_max_index]))
                weather_data[WeatherColumn.T_MIN.value].append(float(row[t_min_index]))
                weather_data[WeatherColumn.PRECIP.value].append(float(row[precip_index]))

            return weather_data
    except (ValueError, IndexError, FileNotFoundError):
        if row_num is not None:
            raise ValueError(f"Row {row_num}: Missing data encountered")
        else:
            raise


def load_pandas_weather(data_file: Path):
    """Parse weather data using pandas"""
    try:
        with open(data_file, encoding="utf-8") as content:
            line_number, _ = _find_header(content)

        # Pandas reader skip_blank_lines is true by default
        # using skiprows instead of header to avoid indexing the incorrect line
        return pd.read_csv(
            data_file,
            skiprows=line_number,
            index_col=WeatherColumn.DATE.value,
            usecols=[
                WeatherColumn.DATE.value,
                WeatherColumn.PRECIP.value,
                WeatherColumn.T_MAX.value,
                WeatherColumn.T_MIN.value,
            ],
            parse_dates=[
                WeatherColumn.DATE.value
            ],
            date_format="%Y-%m-%d"
        )
    except (ValueError, FileNotFoundError) as err:
        raise


def _find_header(content):
    for line_number, line in enumerate(content):
        if (
            WeatherColumn.DATE.value in line
            and WeatherColumn.T_MAX.value in line
            and WeatherColumn.T_MIN.value in line
            and WeatherColumn.PRECIP.value in line
        ):
            return line_number, line
        
    raise ValueError("Header row not found")


if __name__ == "__main__":
    import timeit

    # Benchmarking
    REPS = 5
    EXECUTIONS = 50

    print("Running benchmark - this may take a moment...")

    py_rep = timeit.repeat(
        "load_py_weather(ZOMBA_DATA)", repeat=REPS, number=EXECUTIONS
    )
    pandas_rep = timeit.repeat(
        load_pandas_weather, repeat=REPS, number=EXECUTIONS
    )

    min_py_1 = min(py_rep) / EXECUTIONS
    min_pandas_1 = min(pandas_rep) / EXECUTIONS

    print(f"Pure Python: {min_py_1 * 1000:.3f}ms/rep")
    print(f"Pandas Python: {min_pandas_1 * 1000:.3f}ms/rep")
    print(f"Speedup: {min_py_1/min_pandas_1:.2f}x\n")