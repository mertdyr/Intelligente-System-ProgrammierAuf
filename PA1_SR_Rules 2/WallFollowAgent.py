from is_sr.Agents import Agent8M

class WallFollowAgent(Agent8M):
    """
    Wall-Following Agent according to lecture
    """    
    def __init__(self, memory=False):
        """
        Constructor
        
        Defers construction to Baseclass
        """
        Agent8M.__init__(self, memory)

    @classmethod
    def sense(cls, sensors):
        """
        Generate features from environment using sensor input sensors
        s0 s1 s2
        s7 WF s3
        s6 s5 s4
        """

        """
            STUDENT CODE HERE
        """
        s = sensors
        x1 = 1 if(s[1] == 1 or s[2]== 1) else 0
        x2 = 1 if (s[3] == 1 or s[4] == 1) else 0
        x3 = 1 if (s[5] == 1 or s[6] == 1) else 0
        x4 = 1 if (s[7] == 1 or s[0] == 1) else 0

        x5 = 1 if (s[6] == 1 and s[4] == 1 and s[5] == 0) else 0
        x6 = 1 if (s[0] == 1 and s[2] == 1 and s[1] == 0) else 0
        x7 = 1 if (s[6] == 1 and s[0] == 1 and s[7] == 0) else 0
        x8 = 1 if (s[2] == 1 and s[4] == 1 and s[3] == 0) else 0
        return (x1,x2,x3,x4,x5,x6,x7,x8)
    @classmethod
    def action(cls, x, memory=None):
        """
        Select appropriate rule from rule set based on passed feature vector x

        In some levels memory may be allowed and will be filled with the last executed action.
        """

        """
            STUDENT CODE HERE
        """

        if(x[4]== 1):
            "for the 7th programmiertest"
            return "S"
        elif(x[0]==1 and x[1]==0):
            return "E"
        elif (x[1] == 1 and x[2] == 0):
            return "S"
        elif (x[2] == 1 and x[3] == 0):
            return "W"
        elif (x[3] == 1 and x[0] == 0):
            return "N"
        else:
            return "N"
