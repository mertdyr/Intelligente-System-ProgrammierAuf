import numpy as np
from copy import deepcopy

class Simulation:
    """
    Simulation class handling execution and data acquisition
    """

    @staticmethod
    def block(ax, p, c):
        """
        Put a block of color c in the grid

        Params:
            p: position as numpy array of size 2
            c: color of block

        Return:
            Reference to matplotlib generated element"""
        e = np.array(((0, 0), (0, 1), (1, 1), (1, 0)), dtype=np.intp)
        return ax.fill((p + e)[:, 0], (p + e)[:, 1], c)[0]

    def __init__(self, env, agent, numIter):
        """
        Constructor

        Params:
              env: Level as Environment object
            agent: Agent specification through Agent8M Subclass
             iter: Number of iterations of the simulation
        """
        self.env = deepcopy(env)
        self.agent = agent
        self.numIter = numIter
        self.agents = [deepcopy(agent) for _ in self.env.agentPos]

    def run(self):
        """
        Execute the Simulation

        Returns:
            3 Tuple containing:
                sensors as numpy array of size (2, agent number, iterations)
                commands as numpy array of size (2, agent number, iterations)
                trajectory as numpy array of size(8, agent number, iterations+1)
        """
        trajectory = np.zeros((self.env.numAgents, self.numIter + 1, 2), dtype=np.intp)
        cmds = np.zeros((self.env.numAgents, self.numIter, 2), dtype=np.intp)
        sensors = np.zeros((self.env.numAgents, self.numIter, 8), dtype=np.intp)
        for j in range(self.env.numAgents):
            self.agents[j].setPos(self.env.agentPos[j])
            trajectory[j, 0, :] = self.env.agentPos[j]
        for i in range(self.numIter):
            for j in range(self.env.numAgents):
                sensors[j, i, :] = self.agents[j].getSensorValues(self.env)
                cmds[j, i, :] = self.agents[j].update(sensors[j, i, :])
                trajectory[j, i + 1, :] = self.env.moveRobot(j, cmds[j, i, :])
                self.agents[j].setPos(trajectory[j, i + 1, :])
        self.env.removeAgents()
        return sensors, cmds, trajectory
