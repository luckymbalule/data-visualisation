"""Visualises 2D random walk trajectories using matplotlib"""


import matplotlib.pyplot as plt
from random_walk import RandomWalk


plt.style.use('seaborn-v0_8')
while True:
    rw = RandomWalk()
    
    rw.numpy_walk()
    # rw.py_walk()
    
    points = range(rw.num_points)

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=points,
        cmap=plt.cm.viridis,
        edgecolors=None,
        s=14
    )
    ax.scatter(0, 0, c='green', edgecolors=None, s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors=None, s=200)

    ax.set_aspect('auto')
    plt.show()
    print(plt.get_fignums())
    
    q = input("Regenerate visual? [y/n]: ")
    if q.lower() == "n":
        break