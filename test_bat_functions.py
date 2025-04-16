import pytest
from unittest.mock import patch
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
A test that uses pytest parametrization
to test signal_strength with various distances
"""

@pytest.mark.parametrize(
    "distance, expected",
    [(0, 100), (5, 50), (10,0), (12, 0)]
)
def signal_strength(distance, expected):

    assert signal_strength(distance) == expected

"""
A pytest.fixture that sets up a reusable dictionary
of bat vehicles 
"""
@pytest.fixture
def bat_vehicles():
    return {
        'Batmobile' : {'speed': 200, 'armor':80},
        'Batwing' : {'speed': 300, 'armor': 60},
        'Batcycle' : {'speed': 150, 'armor': 50}
    }

"""
A test that returns correct specifications 
for known vehicles 
"""
def test_get_known_vehicle(bat_vehicles: dict[str, dict[str, int]]):
    for name, expected_specs in bat_vehicles.items():
        result = get_bat_vehicle(name)
        assert result == expected_specs, f"Expected specs for {name} do not match."

"""
A test that raises error for the unknown vehicles
"""
def test_get_invalid_bat_vehicle(bat_vehicles):
    invalid_names = ["Batbike", "Batboat", "Batmarine", "", "bt", "batmobil", "BATMOBILE"]

    for name in invalid_names:
        assert name not in bat_vehicles
        with pytest.raises(ValueError, match=r"Unknown vehicle: .*"):
            get_bat_vehicle(name)

"""
A test that is mocking the entire function without using delay
and returning a custom dictionary
"""

def test_mock_fetch_joker_info(mocker):
    mock_response = {'mischief_level': 0, 'location': 'captured'}

    mocker.patch("bat_functions.fetch_joker_info", return_value=mock_response)
    
    result = fetch_joker_info()

    assert result == mock_response