import numpy as np

class Environment:
    """
    Grid environment class

    Provides mechanism for agents to move, check movement and detect presence of barriers and other agents

    field contains the actual grid definition with the following content:
    0 - free
    1 - barrier
    2 - agent
    """

    def __init__(self, number, name, size, start, enclosed=True, tight=False):
        """
        Constructor

        Params:
            size: size of grid as 2 element vectot/list/tuple
            start: List of 2 element tuples/arrays with starting locations (Also defines agent count)
        """
        self.number = number
        self.name = name
        self.tight = tight
        self.field = np.zeros(size, dtype=np.intp)
        start = np.array(start)
        if len(start.shape) == 1:
            self.numAgents = 1
            self.agentPos = np.array([start], dtype=np.intp)
        else:
            self.numAgents = start.shape[0]
            self.agentPos = start
        for i in range(self.numAgents):
            self.field[(self.agentPos[i, 0], self.agentPos[i, 1])] = 2
        self.enclosed = enclosed

    def isBlocked(self, pos):
        """
        Check for blockage of a cell

        Params:
            pos: Cell position as numpy array of size 2
        Return:
            True if blocked, False otherwise
        """

        # if enclosed sensors check the opposite side of the map
        if not self.enclosed:
            if pos[0] == self.field.shape[0]:
                pos[0] = 0
            elif pos[0] == -1:
                pos[0] = self.field.shape[0] - 1

            if pos[1] == self.field.shape[1]:
                pos[1] = 0
            elif pos[1] == -1:
                pos[1] = self.field.shape[1] - 1

        # if not enclosed and agent is at border, it is blocked
        elif (np.minimum(np.maximum(pos, np.zeros(2)), self.field.shape - np.array((1, 1), dtype=np.intp)) != pos).any():
            return True

        return self.field[(pos[0], pos[1])] != 0

    def isRobot(self, pos):
        """
        Check if a cell contains a robot/agent

        Params:
            pos: Cell position as numpy array of size 2
        Returns:
            True if robot/agent at this cell, False otherwise
        """
        return self.field[pos] == 2

    def agentPos(self, i):
        """
        Returns the specified agent's position

        Params:
            i: Index of agent/robot
        Returns:
            numpy array of size 2 containing position of agent/robot
        """
        return self.agentPos[i]

    def moveRobot(self, i, cmd):
        """
        Move the robot/agent
        Only move the robot is the target cell is free. Otherwise no movement is done.

        Params:
              i: Index of agent/robot
            cmd: Movement command as numpy vector of size 2
        Returns:
            New position of agent/robot as numpy array of size 2
        """

        new_pos = self.agentPos[i] + cmd

        # if map is not enclosed, check if agent tries to cross border and correct new position
        if not self.enclosed:
            if new_pos[0] == self.field.shape[0]:
                new_pos[0] = 0
            elif new_pos[0] == -1:
                new_pos[0] = self.field.shape[0] - 1

            if new_pos[1] == self.field.shape[1]:
                new_pos[1] = 0
            elif new_pos[1] == -1:
                new_pos[1] = self.field.shape[1] - 1

        # if map is enclosed, don't update the position
        elif (np.minimum(np.maximum(new_pos, np.zeros(2)), self.field.shape - np.array((1, 1), dtype=np.intp)) != new_pos).any():
            self.agentPos = np.minimum(np.maximum(self.agentPos, np.zeros(2, dtype=np.intp)),
                                       self.field.shape - np.array((1, 1), dtype=np.intp))

        # if the new position is not blocked, move
        if not self.isBlocked(new_pos):
            self.field[(self.agentPos[i, 0], self.agentPos[i, 1])] = 0
            self.agentPos[i] = new_pos
            self.field[(self.agentPos[i, 0], self.agentPos[i, 1])] = 2

        return self.agentPos[i]

    def removeAgents(self):
        self.field[self.field == 2] = 0

    def __str__(self):
        return f"Level {self.number}: {self.name}"
