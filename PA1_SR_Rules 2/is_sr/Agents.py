import numpy as np

class Agent8M:
    """
    Template class for agents / robots
    """
    
    east  = np.array(( 1, 0), dtype = np.intp)
    south = np.array(( 0,-1), dtype = np.intp)
    west  = np.array((-1, 0), dtype = np.intp)
    north = np.array(( 0, 1), dtype = np.intp)
    actions = {"E": east, "S": south, "W": west, "N": north}
    sensors = np.array((
                    (-1, 1), # NW
                    ( 0, 1), # N
                    ( 1, 1), # NE
                    ( 1, 0), # E
                    ( 1,-1), # SE
                    ( 0,-1), # S
                    (-1,-1), # SW
                    (-1, 0)  # W
                ), dtype=np.intp)

    def __init__(self, memory=False):
        """
        Constructor
        
        Initializes agent to position (0,0) and registers commands: east, south, west, north

        Optionally initializes memory
        """
        self.pos = np.zeros(2)
        
        if memory:
            self.memory = None
        
    def setPos(self, pos):
        """
        Set position of agent
        
        Gets called from the Environment
        
        Params:
            pos: new position of agent as numpy array of size 2
        """
        self.pos = np.array(pos)
        
    def getSensorValues(self, level):
        """
        Akquire sensor values
        
        Gets called from the simulation
        
        params:
            level: Evironment containing the level
        
        Returns:
            numpy array of size 8 containing 1 for blocked and 0 for free
        """
        return np.array([level.isBlocked(self.pos + sensor) for sensor in self.sensors])

    @classmethod
    def action(cls, x, memory = None):
        raise RuntimeError("action() not implemented for base Agent8M")

    @classmethod
    def sense(cls, sensors):
        raise RuntimeError("sense() not implemented for base Agent8M")

    
    def update(self, sensors):
        """
        Generate features from environment and execute rule set
        """

        x = self.sense(sensors)

        if hasattr(self, "memory"):
            action = self.action(x, self.memory)
            self.memory = action
        else:
            action = self.action(x)
            
        return self.actions[action]

    def __str__(self):
        """
        Convert agent to string representation
        
        Returns:
            Agent description string
        """
        return "NavAgent at %s" % self.pos
