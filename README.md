# UnitTestingPython — Testing Batman's Toolkit

## Overview

This is a Unit Testing in python project focused on applying modern testing practises using pytest framework to verify the correctness and robustness of a module called bat_functions.py, which includes fictional functionalities inspired by the Batman universe.

## My Approach

To complete the assignment, I adopted a clean and modular development strategy. I created a dedicated barnch (bat-tests) to isolate my testing work from the main branch and progressively implemented tests for each function in bat_functions.py. I began by writing basic unit tests with pytest, using fixtures to eliminate duplication and ensure consistent test data. For edge cases and error handling, I used pytest.raises to verify exception behavior. I mocked external dependencies like fetch_joker_info() using pytest-mock, ensuring my tests remained fast and detrerministic. Finally, I set up Continuous Integration via GitHub Actions to automatically run the test suite on every push or pull request, ensuring ongoing code quality and immediate feedback on changes.

## Application Details

    - Python 3.10
    - pytest - for unit testing
    - pytest-mock - for mocking dependencies
    - GitHub Actions - for CI (runs tests on every push)

## Implemented tests

    - **calculate_bat_power(level)**
      Checks if Batman's power level is calculated correctly using simple assertions.

    - **signal_strength(distance)**
      Tests how signal strength degrades with distance (including edge cases) using simple assertions.

    - **get_bat_vehicle(vehicle_name)**
      Validates vehicle lookup and error handling for unknown entries using fixtures.

    - **fetch_joker_info()**
      Uses mocking to simulate an API call, avoid delays and return custom mock data.

    ## Running Tests Locally

    1) Clone the repository: git clone https://github.com/MariosLiapis/bat-test-assignment.git

    2) Install dependencies: pip install pytest pytest-mock

    3) Run the tests: pytest