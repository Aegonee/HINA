# 2024.3.26 created by: An Chang
import re

def FindDigits(string):
    res = re.findall(r"-?\d+\.?\d*[eE]?-?\d*", string)
    return res
