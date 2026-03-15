import traceback
import numpy as np

from .Simulation import Simulation

class Test:

    def toSets(data, offset):
        return [set([tuple(x) for x in data[agentID, offset:, :]]) for agentID in range(data.shape[0])]
    
    def __init__(self, sim):
        self.sim = sim

    def run(self):
        try:
            _, _, trajectory = self.sim.run()
            itOffset = 6
            refData = np.load(f"level{self.sim.env.number}_test_data.npy")
            ref = Test.toSets(refData, itOffset)
            result = Test.toSets(trajectory, itOffset)
            if ref != result:
                print(f"{self.sim.agent.__class__.__name__} failed {self.sim.env} - Visited Positions were:\n\t{result}\n\tShould be:\n\t{ref}")
                return False
            return True
        except:
            traceback.print_exc()

def runTests(levels, agent_class):
    result = True
    for level in levels:
        sim = Simulation(level, agent_class(level.tight), 100)
        testResult = Test(sim).run()
        print("Level", level.number, "->", testResult)
        result = testResult and result
    return result
