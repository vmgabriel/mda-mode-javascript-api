"""
Module of Concat Handler Data
"""

# Libraries
from typing import Callable
from src.outputs.handlers.conversor import conversors
from src.outputs.handlers.filter import filters


def type_data(structure: dict) -> Callable:
    """Type Data Model"""
    def type_mode(_s: object) -> str:
        """
        Maps type names from PrimitiveType to entity
        """
        return structure.get(_s.name, _s.name)
    return type_mode


def verify_model(entity_model: object) -> Callable:
    """Verify Data of Model"""

    def is_entity(entity: object) -> bool:
        """
        Test to prove if some type is an entity
        """
        return entity.type in entity_model.entities
    return is_entity


handlers = {
    'conversors': conversors,
    'filters': filters,
    'type_data': type_data,
    'verify_model': verify_model,
}
