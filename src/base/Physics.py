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

    def __init__(self, disp):
        self.disp_x = disp

class Stress:
    sigma_xx = 0.0
    sigma_yy = 0.0
    sigma_zz = 0.0
    sigma_xy = 0.0
    sigma_xz = 0.0
    sigma_yz = 0.0

    def __init__(self):
        pass

class Strain:
    epsilon_xx = 0.0
    epsilon_yy = 0.0
    epsilon_zz = 0.0
    epsilon_xy = 0.0
    epsilon_xz = 0.0
    epsilon_yz = 0.0

    def __init__(self):
        pass