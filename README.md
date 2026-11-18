# Data Visualisation

This project covers data visualisation of Python Crash Course (3rd) exploring data generation, creating visualisations using plotly and matplotlib, and performance optimisation e.g. Numpy vectorisation.

## Chapters covered

### Chapter 15 - Generating Data
`src/generated/`

* `random_walk.py` & `rw_visual.py`:
  * `RandomWalk` class: generates spatial random walk trajectories
    - Benchmarking Results (Pure python vs Numpy vectorisation) - numpy scales better at large scale `num_points`
  * `rw_visual.py`: visualises 2D spatial random walk using Matplotlib

* `die.py` & `die_visual.py` - `Die` class & `roll_die()` and `roll_dice()` visualising roll probability distribution
  * `Die` class: represents a single die with customisable side count
  * `roll_die()`: generates a single die roll probability using plotly
  * `roll_dice()`: generates multiple dice roll probability using pandas

### Chapter 16 - Downloading Data
`src/downloaded/`

* `weather_loader.py` & `weather_plotter.py`:
  * `load_py_weather()`: parses a weather CSV with the `csv` module and returns a list
  * `load_pandas_weather()`: parses a weather CSV with pandas, returning a DataFrame
  * `plot_py_weather()`: loads weather data (list) and plots daily highs and lows
  * `plot_pandas_weather()`: loads weather DataFrame and plots monthly rainfall

* `earthquake_viz.py`:
  * `load_py()` & `load_pandas()`: extract magnitudes, coordinates, title, and marker sizes
  * `plot_eq()`: generates a scatter geo map (marker scaling at `2 ** magnitude`)

## Run

Scripts can be run from the project root or from within their directory. Generated plots are automatically saved to `outputs/`

```bash
pip install matplotlib numpy plotly pandas
```

Chapter 15
```bash
# Run random walk benchmark test suite
python src/generated/random_walk.py

# Execute random walk visualiser
python src/generated/rw_visual.py

# Execute die roll probability visualiser
python src/generated/die_visual.py
```

Chapter 16
```bash
# Run weather data parsing benchmark
python src/downloaded/weather_loader.py

# Plot weather data
python src/downloaded/weather_plotter.py

# Plot earthquake
python src/downloaded/earthquake_viz.py
```