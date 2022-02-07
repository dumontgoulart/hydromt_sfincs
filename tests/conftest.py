"""add global fixtures"""

import pytest
import numpy as np

@pytest.fixture
def weirs():
    feats = [
        {
            "name": "WEIR01",
            "x": [0, 10, 20],
            "y": [100, 100, 100],
            "z": 5.0,
            "par1": 0.6,
        },
        {
            "x": [100, 110, 120],
            "y": [100, 100, 100],
            "z": [5.0, 5.1, 5.0],
            "par1": 0.6,
        },
    ]
    return feats

@pytest.fixture
def elevation_data():
    # make coordinates
    xi, yi = np.meshgrid(np.linspace(0, 100, 11), np.linspace(0, 100, 11) + 10)
    # make some variables scaled from zero to 2*pi
    x_var = (xi - xi.min()) / (xi.max() - xi.min()) * 2 * np.pi
    y_var = (yi - yi.min()) / (yi.max() - yi.min()) * 2 * np.pi
    # random goniometrics to make elevation values (including some
    elevation = -3 * np.cos(x_var) ** 2 + 5 * np.arctan(y_var) ** 2 + 2 * np.sin(x_var * y_var)
    data = {
        "xi": xi,
        "yi": yi,
        "elevation": elevation,
    }
    return data

@pytest.fixture
def manning_data():
    xi, yi = np.meshgrid(np.linspace(0, 100, 11), np.linspace(0, 100, 11) + 10)
    manning = np.ones(xi.shape)*0.07 + xi/7000 - yi/8000
    data = {
        "xi": xi,
        "yi": yi,
        "manning": manning
    }
    return data