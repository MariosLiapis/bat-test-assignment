import pytest
from bat_functions import *

"""
A function that verifies calculate_bat_power 
returns the correct power for different levels
"""

def calculate_bat_power():

    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(5) == 210
    assert calculate_bat_power(-2) == -84


"""
A function that uses pytest parametrization
to test signal_strength with various distances
"""

@pytest.mark.parametrize(
    "distance, expected",
    [(0, 100), (5, 50), (10,0), (12, 0)]
)
def signal_strength(distance, expected):

    assert signal_strength(distance) == expected