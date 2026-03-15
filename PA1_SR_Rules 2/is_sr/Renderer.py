import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import ArtistAnimation
from .Simulation import Simulation


def RenderSimulation(sim: Simulation, trajectory):
    """
    Render the trajectories of the agents

    Params:
        trajectory: numpy array containing trajectory of agents/robots

    Returns:
        An animation object of matplotlib
    """
    images = []
    fig, ax = plt.subplots()

    X = sim.env.field.shape[0]
    Y = sim.env.field.shape[1]

    ax.set_xlim(-1, X + 1)
    ax.set_ylim(-1, Y + 1)
    ax.set_title(f"Level {sim.env.number}: {sim.env.name}")

    ax.set_xticklabels([])
    ax.set_xticks(np.arange(0, X + 0.5))
    ax.set_yticklabels([])
    ax.set_yticks(np.arange(0, Y + 0.5))
    min_x, max_x, min_y, max_y = (-1, X + 1, -1, Y + 1) if sim.env.enclosed else (0, X, 0, Y)
    ax.vlines(range(min_x, max_x), min_y, max_y, "grey")
    ax.hlines(range(min_y, max_y), min_x, max_x, "grey")
    if sim.env.enclosed:
        for x in range(-1, X + 1):
            Simulation.block(ax, np.array((x, -1), dtype=np.intp), "black")
            Simulation.block(ax, np.array((x, Y), dtype=np.intp), "black")
        for y in range(-1, Y + 1):
            Simulation.block(ax, np.array((-1, y), dtype=np.intp), "black")
            Simulation.block(ax, np.array((X, y), dtype=np.intp), "black")

    for l in np.transpose(np.where(sim.env.field == 1)):
        Simulation.block(ax, l, "black")

    for i in range(0, sim.numIter + 1):
        output = []
        for j in range(len(sim.agents)):
            output += RenderAgent(sim.agents[j], ax, trajectory[j, i, :], sim.env)
        images.append(output)

    return ArtistAnimation(fig, images, interval=200)


def RenderAgent(agent, ax, p, level):
    """
    Render the agent into the grid

    Params:
        ax: Matplotlib Axis object
        p: Position of agent as numpy array of size 2
        level: Environment containing level
    Returns:
        Generated Matplotlib object
    """
    lines = []
    for v in p + agent.sensors:
        o = np.array((0.5, 0.5))
        a = np.stack((p + o, v + o))
        if not level.isBlocked(v):
            lines.append(ax.plot(a[:, 0], a[:, 1], color="blue")[0])
        else:
            lines.append(ax.plot(a[:, 0], a[:, 1], color="yellow")[0])
    lines.append(Simulation.block(ax, p, "blue"))
    return lines
