# 2024.4.15 created by: An Chang
import pandas
from src.base.exceptions import HINAExceptions
from enum import Enum

# TODO: redefine exception class

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

class Parser(Loader):

    message = []
    type = ""

    def __init__(self, message):
        self.type = ""
        self.message = message

    def GetMessage(self, loader):
        if isinstance(loader.type, HINAExceptions):
            try:
                rcode = loader.Dump(self.message)
            except:
                return HINAExceptions.HINAValueError
        else:
            return HINAExceptions.HINAValueError

    def Dump2FrameSeries(self, FrameSeries):
        match self.type:
            case "txt":
                pass
            case "csv":
                pass
