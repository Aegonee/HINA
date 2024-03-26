# 2024.3.26 created by: An Chang

import sys
import numpy
sys.path.append("./src/base/")
from src.base.Physics import Timestamp, Acc, Vel

class Frame:

    cur_timestamp = Timestamp(0);
    acc = 0.0           # second
    vel = 0.0           # m/s
    disp = 0.0          # m/s^2

    K = 0.0
    C = 0.0

    # def __init__(self, timestamp):
    #     self.cur_timestamp = Timestamp(0)
    #     pass

    def __init__(self, timestamp, acc = 0.0, vel = 0.0, disp = 0.0):
        self.cur_timestamp = Timestamp(0)
        self.acc = acc
        self.vel = vel
        self.disp = disp

    @staticmethod
    def GetInstance():
        pass
    
class FrameSeries:

    frames = []
    start_timestamp = 0
    end_timestamp = 0
    
    def __init__(self):
        pass

    def ParserIn(self, array):
        # TODO: add logic: translate numpy array to Frame and FrameSeries
        pass

    def ParserOut(self):
        # TODO: add logic: publish as ndarray
        # consider: if necessary to add publish nodes?
        pass