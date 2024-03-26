# 2024.3.26 created by: An Chang

class Dimension:
    DIMENSION_1 = 1
    DIMENSION_2 = 2
    DIMENSION_3 = 3
    DIMENSION_ELSE = 0

    def SetDimension(self, dim):
        self.DIMENSION_ELSE = dim
        
    
class Timestamp:
    ts_second = 0
    def __init__(self, ts):
        self.ts_second = ts


class Acc:
    acc_x = 0.0
    acc_y = 0.0
    acc_z = 0.0
    def __init__(self, acc):
        self.acc_x = acc

class Vel:
    vel_x = 0.0
    vel_y = 0.0
    vel_z = 0.0

    def __init__(self, vel):
        self.vel_x = vel

class Disp:
    disp_x = 0.0
    disp_y = 0.0
    disp_z = 0.0

    def __init(self, disp):
        self.disp = disp
