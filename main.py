# 2024.3.26 created by: An Chang

from src.base.Frame import Frame, FrameSeries
from src.base.physics import Acc, Vel, Disp, Dimension, Timestamp
from src.common.math_utils import MergeInterval
from src.common.dataloader import Loader, Parser
import pandas
import numpy as np


if __name__ == "__main__":
    path = "./data/"
    csv_name = "data.csv"

    readf = pandas.read_csv(path + csv_name)

    headers = readf.columns.tolist()