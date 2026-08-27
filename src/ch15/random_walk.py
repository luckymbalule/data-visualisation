"""
Random Walk Generator and Perfomance Benchmark

Provides a class for generating independent 1D arrays for X and Y axes using
Pure python loops and vectorised Numpy operation 
"""


from random import choice
import numpy as np


class RandomWalk:
    """Generates independent 1D walk points for X and Y axes"""
    def __init__(self, num_points=5000):
        """Initialise class"""
        self.num_points = num_points

    def py_walk(self):
        """Generate axes values using standard python loops"""
        directions = (1, -1)
        steps = (0,1,2,3,4)
        self.x_values = [0]
        self.y_values = [0]

        while self.num_points > len(self.x_values):
            x_step = choice(directions) * choice(steps)
            y_step = choice(directions) * choice(steps)

            if y_step == 0 and x_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def numpy_walk(self):
        """Generate axes values using Numpy vectorisation"""
        directions = np.array([1,-1])
        magnitude = np.array([0,1,2,3,4])
        asize = self.num_points - 1
        rng = np.random.default_rng()

        x_steps = (
            rng.choice(directions, size=asize) * rng.choice(magnitude, size=asize)
        )
        y_steps = (
            rng.choice(directions, size=asize) * rng.choice(magnitude, size=asize)
        )

        mask = (x_steps == 0) & (y_steps == 0)

        while np.sum(mask) > 0:
            msize = np.sum(mask)
            x_steps[mask] = (
                rng.choice(directions, size=msize)
                * rng.choice(magnitude, size=msize)
            )
            y_steps[mask] = (
                rng.choice(directions, size=msize)
                * rng.choice(magnitude, size=msize)
            )

            mask = (x_steps == 0) & (y_steps == 0)

        self.x_values = np.concatenate(([0], np.cumsum(x_steps)))
        self.y_values = np.concatenate(([0], np.cumsum(y_steps)))


# Benchmarking
if __name__ == '__main__':
    import timeit

    REPS = 5
    EXECUTIONS = 10
    NUM_POINTS = 50_000

    def run_py_walk():
        rw = RandomWalk(NUM_POINTS)
        rw.py_walk()

    def run_numpy_walk():
        rw = RandomWalk(NUM_POINTS)
        rw.numpy_walk()

    # Run n-times [REPS] test batch - for reliable comparative testing
    py_reps = timeit.repeat(run_py_walk, repeat=REPS, number=EXECUTIONS)
    numpy_reps = timeit.repeat(run_numpy_walk, repeat=REPS, number=EXECUTIONS)

    # Use min() to filter out system noise 
    min_py_rep = min(py_reps) / EXECUTIONS
    min_numpy_rep = min(numpy_reps) / EXECUTIONS

    print(f"Pure Python: {min_py_rep * 1000:.3f} ms/walk")
    print(f"Numpy: {min_numpy_rep * 1000:.3f} ms/walk")
    print(f"Speedup: {(min_py_rep/min_numpy_rep):.2f}x")