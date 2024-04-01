# 2024.3.26 created by: An Chang

import numpy
import pandas
import sys
sys.path.append("./src/base/")
from ..base.Physics import Timestamp, Dimension

class Swarm:
    velocity = []
    position = []
    dimension = 1

    def __init__(self, dimension = 1):
        self.dimension = dimension
        self.velocity = [0 for i in range(dimension)]
        self.position = [0.0 for i in range(dimension)]


class SwarmOptim:
    # Problem Scale
    particle_num = 10
    partical_demension = 1
    time_step = 0.0

    # Swarm
    particles = []
    global_optimized_particle = Swarm(1)

    # Algorithm Parameters
    max_allowed_error = 0.1
    recur_times = 0
    inertia_weight = 0
    individual_param = [2]
    social_param = 2
    scalor = [1]

    # Swarm Qualities
    # TODO: define appropriate form of Qualities params
    velocity_limit = []
    solution_space_limit = []
    fitness_values = []

    def __init__(self, dimension = 1):
        self.Reset(dimension = dimension)

    def Solve(self):
        for i in range(self.recur_times):
            self.FitnessEvaluate()
            self.FindGlobalBest()
            if self.Judge():
                return
        return

    def FitnessEvaluate(self, fit_func = lambda: None):
        self.fitness_values = fit_func(self)
        # TODO: define fit_func
        return

    def Reset(self, need_init = 0, dimension = 1, random_func = lambda: None):
        if need_init:
            self.Init(random_func = random_func)
        '''
        if random_func:
            random_func(self.particle_num, self.solution_space_limit)
        '''
                # TODO: finish random func: define as class method or function
        self.particles = [Swarm(dimension) for i in range(self.particle_num)]
        self.fitness_values = [0 for i in range(self.particle_num)]
        return
    
    def Init(self, random_func = lambda: None):
        random_func(self.particle_num, self.solution_space_limit)
        # TODO: add logic: randomrize velocity and position
        # TODO: decide: whether random_func need to be defined in class SwarmOptim or in MathUtils
        return

    def UpdateIndividual(self):
        # TODO: add logic: updata best position of individuals
        pass

    def UpdateSociety(self):
        # TODO: add logic: update global best position
        pass
    
    def FindGlobalBest(self):
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
    