from typing import Any
import operator
import sys
import os

class Something:
    def __init__(self, var_one: str, var_two: Any):
        print(self)
    
    def __call__(self):
        print('this has been called')