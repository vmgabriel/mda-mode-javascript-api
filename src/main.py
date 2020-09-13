"""
Module Control For Init Project
"""

from src.config import configuration
from src.utils import utils


def load():
    """Load a Project"""
    print('- Configuration Routes -')
    print(configuration)
    print(utils.get('inputs')
          .get('read_json_file')(
              configuration.get('templates')
              .get('template_configuration')
          ))
    print('- Configuration Routes -')
