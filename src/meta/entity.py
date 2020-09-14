"""
Module for Meta-Programming read
"""

# Libraries
from os.path import join, dirname
from textx import metamodel_from_file

this_folder = dirname(__file__)


class SimpleType(object):
    """
    Simple Type Class Definition
    """
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def __str__(self):
        return self.name


type_builtins = {
        'number': SimpleType(None, 'integer'),
        'string': SimpleType(None, 'string'),
        'float': SimpleType(None, 'string'),
        'datetime': SimpleType(None, 'datetime'),
        'date': SimpleType(None, 'date'),
        'time': SimpleType(None, 'time'),
        'boolean': SimpleType(None, 'boolean'),
    }


def get_entity_mm(file_name: str, debug=False):
    """
    Get Entity Meta Model
    """
    entity_mm = metamodel_from_file(
        join(this_folder, 'entity.tx'),
        classes=[SimpleType],
        builtins=type_builtins,
        debug=debug
    )

    return entity_mm.model_from_file(file_name)
