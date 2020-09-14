"""
Module for System Execute
"""

# Libraries
from os import mkdir
from os.path import exists


def create_path(path: str) -> None:
    """
    Create A Path If not Exists
    """
    if not exists(path):
        mkdir(path)

system = {
    "create_path": create_path
}
