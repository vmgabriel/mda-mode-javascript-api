"""
Module for JSON Read
"""

# Libraries
import json


def read_json_file(name_file: str) -> dict:
    """Read a JSON File
    @params name_file: str -> Data file
    @return: dict -> the Data of File
    """
    try:
        file = open(name_file, 'rt')
        data_file = json.load(file)
        return data_file
    except FileExistsError:
        print('[Error] - File Not Exist')
    finally:
        file.close()
