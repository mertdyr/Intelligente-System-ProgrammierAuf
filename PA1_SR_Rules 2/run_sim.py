#!/usr/bin/env python3

import sys

import matplotlib.pyplot as plt

from is_sr.Simulation import Simulation
from is_sr import Renderer
from is_sr.Levels import levels

from WallFollowAgent import WallFollowAgent

level = levels[int(sys.argv[1])-1]

sim = Simulation(level, WallFollowAgent(level.tight), 100)

sensors, cmds, trajectory = sim.run()
ani = Renderer.RenderSimulation(sim, trajectory)

plt.show()
