# 2024.3.26 created by: An Chang
import numpy as np
from enum import Enum


class RandMode(Enum):
    NORMAL = 0
    UNIFORM = 1


class BoundaryType(Enum):
    UPPER = 0
    LOWER = 1


def FindMaxGrad():
    pass


def RandomDistribute(boundaries, pts, dimension, rand_mode=RandMode.NORMAL):
    dimension = len(boundaries)
    pts_num = len(pts)
    match rand_mode:
        case RandMode.NORMAL:
            rand_func = np.random.normal
        case RandMode.UNIFORM:
            rand_func = np.random.uniform
        case _:
            # TODO: define customorized exception
            raise ValueError(
                "Invalid Random Mode",
            )
    pts = [
        [
            rand_func(
                boundaries[BoundaryType.UPPER.value][i],
                boundaries[BoundaryType.LOWER.value][i],
            )
            for i in range(dimension)
        ]
        for j in range(pts_num)
    ]


def MergeInterval():
    pass
