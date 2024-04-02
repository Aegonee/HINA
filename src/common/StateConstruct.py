# 2024.4.2 created by: An Chang

from ..base.Frame import Frame, FrameSeries

class StateSpace:

    frame_series = FrameSeries()

    def __init__(self, Frames):
        self.frame_series = Frames