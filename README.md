# Data Visualisation

This project covers data visualisation of PCC3 exploring data generation, creating a series of visualisation using plotly and matplotlib, and performance optimisation e.g. Numpy vectorisation.

## Chapters covered

### Chapter 15 — Generating Data

* `random_walk.py` & `rw_visual`:
  * `RandomWalk` class: Generates spatial random walk trajectories
    - Benchmarking Results (Pure python vs Numpy vectorisation) - numpy scales better at large scale `num_points`
  * `rw_visual.py`: Visualises 2D spatial random walk using Matplotlib

* `die.py` & `die_visual.py` - `Die` class & `roll_die()` and `roll_dice()` visualising roll probability distribution
  * `Die` class: represents a single die with customisable side count
  * `roll_die()`: Generates a single die roll probability using plotly
  * `roll_dice()`: Generates multiple dice roll probability using pandas

## Run

Scripts can be run from the project root or from within ther directory. Generated plots are automatically saved to `outputs/`

```bash
pip install matplotlib numpy plotly pandas
```

Chapter 15
```bash
# Run random walk benchmark test suite
python src/ch15/random_walk.py

# Execute random walk visualiser
python src/ch15/rw_visual.py

# Execute die roll probability visualiser
python src/ch15/die_visual.py
```