"""
Module Control For Init Project
"""
# Libraries
import os
from typing import Callable
from src.config import configuration
from src.utils import utils

fn_read_json_file = utils.get('inputs').get('read_json_file')


def read_template(template_path: str) -> Callable:
    """Read Template"""

    def read_module(module: dict) -> dict:
        """Get Module to Template"""
        print('Template Path - ', template_path)
        print('module - ', module)
        module.update({
            'path_complete': os.path.join(template_path, module.get('path')),
            'configuration_base': os.path.join(
                template_path,
                module.get('path'),
                module.get('file_configuration')
            ),
        })
        module.update({
            'configuration_plugin': fn_read_json_file(
                module.get('configuration_base')
            )
        })
        return module

    return read_module


def load():
    """Load a Project"""
    print('- Configuration Routes -')
    template_configuration = configuration.get('templates').get(
        'template_configuration'
    )
    template_path = configuration.get('templates').get(
        'template_path'
    )
    plugin_configuration = fn_read_json_file(template_configuration)
    plugin_configuration = list(
        map(
            read_template(template_path),
            plugin_configuration.get('modules')
        )
    )
    print('Plugin Configuration - ', plugin_configuration)
    print('- Configuration Routes -')
