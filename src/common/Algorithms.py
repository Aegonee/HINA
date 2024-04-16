import re


def FindDigits(string):
    res = re.findall(r"-?\d+\.?\d*[eE]?-?\d*", string)
    return res
