# 2024.4.15 created by: An Chang
import pandas
from src.base.Exceptions import HINAExceptions


class Loader:

    path = "default.txt"
    message = ()
    type = "txt"

    def __init__(self, path):
        self.path = path
        self.GetType()

    def GetType(self):
        split_path = self.path.split('.')
        self.type = split_path[-1]

    def csvLoader(self):
        try:
            pandas.read_csv(self.path)
        except:
            return HINAExceptions.HINAPathError
        return HINAExceptions.HINASuccessCode

    def DefaultLoader(self):
        try:
            with open(self.path) as f:
                self.message = f.readlines()
        except:
            return HINAExceptions.HINAPathError
        return HINAExceptions.HINASuccessCode

    def Dump(self, target):
        if self.message:
            target = self.message
            return HINAExceptions.HINASuccessCode
        else:
            return HINAExceptions.HINAValueError
