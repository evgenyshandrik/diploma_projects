"""
Module for work with resources
"""
import tests
from pathlib import Path


def path(relative_path):
    """
    Get path to resource file
    """
    return (
        Path(tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )