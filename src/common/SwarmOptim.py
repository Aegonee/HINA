# 2024.3.26 created by: An Chang

import numpy as np
import pandas
import sys
import random
sys.path.append("./src/base/")
from ..base.Physics import Timestamp, Dimension
from ..base.MathUtils import RandomDistribute, RandMode

class Swarm:
    velocity = []
    position = []
    dimension = 1

    def __init__(self, postition = [], velocity = [], dimension=1):
        self.dimension = dimension
        if postition.empty():
            self.velocity = [0 for i in range(dimension)]
        if velocity.empty():
            self.position = [0.0 for i in range(dimension)]


class SwarmOptim:
    # Problem Scale
    particle_num = 10
    partical_demension = 1
    time_step = 0.0

    # Swarm
    # TODO: refactor with Swarm
    particles = []
    global_optimized_particle = Swarm(1)
    velocity = []
    dimension = 1
    position = []

    # Algorithm Parameters
    max_allowed_error = 0.1
    recur_times = 0
    inertia_weight = 0.9
    individual_param = [2]  # c1
    social_param = 2  # c2
    scalor = [1]
    random_param = []

    # Swarm Qualities
    # TODO: define appropriate form of Qualities params
    velocity_limit = []
    solution_space_limit = []
    fitness_values = []
    pbest = []
    gbest = []

    def __init__(self, dimension=1):
        self.Reset(dimension=dimension)

    def __len__(self):
        return self.particle_num

    def Solve(self, is_greedy=False, is_mutate=False):
        for i in range(self.recur_times):
            self.Update(is_mutate=is_mutate)
            if self.Judge():
                return
        return

    def Update(self, is_mutate=False):
        self.FitnessEvaluate()
        self.UpdateBestLocation()
        self.UpdateVelocity()
        self.UpdateInertia()
        if is_mutate:
            self.Mutate()

    def FitnessEvaluate(self, fit_func=lambda: None):
        self.fitness_values = [fit_func(self.particles[i]) for i in range(self.dimension)]
        return

    def Reset(self, need_init=0, dimension=1, random_mode=RandMode.NORMAL):
        if need_init:
            self.Init(rand_mode=random_mode)
        """
        if random_func:
            random_func(self.particle_num, self.solution_space_limit)
        """
        # TODO: finish random func: define as class method or function
        self.particles = [Swarm(dimension) for i in range(self.particle_num)]
        self.fitness_values = [0 for i in range(self.particle_num)]
        return

    def Init(self, rand_mode=RandMode.NORMAL):
        coords = [[0.0 for i in range(self.dimension)] for j in range(self.particle_num)]
        RandomDistribute(self.solution_space_limit, coords, self.dimension, rand_mode=RandMode.NORMAL)
        self.particles = [Swarm(postition=coords[i], velocity=[0.0 for j in range(self.dimension)], dimension=self.dimension) for i in range(len(coords))]
        self.UpdateVelocity()
        self.UpdateBestLocation()
        self.UpdateInertia()
        # TODO: add logic: randomrize velocity and position
        # TODO: decide: whether random_func need to be defined in class SwarmOptim or in MathUtils
        return

    def UpdateVelocity(self, param_size=2):
        self.random_param.clear()
        self.random_param = [random.uniform(0, 1) for i in range(param_size)]
        # self.velocity = [SwarmOptim.CalcCurVelocity(self.v[i], self.inertia_weight[i], self.individual_param[i], self.social_param, self.random_param[0], self.random_param[1]) for i in range(self.particle_num)]
        # TODO: add logic: updata best position of individuals
        pass

    def UpdateBestLocation(self):
        # TODO: add logic: update global best position
        pass

    def UpdateInertia(self):
        # TODO: add logic: some kind of sort function
        pass

    def Judge(self):
        # TODO: verify: if necessary
        pass

    def Mutate(self):
        # TODO: add mutate logic
        pass

    def LimitRange(self):
        # TODO: verify: if necessary
        pass

    def CurVelocity(self):
        
        pass
