"""
Module Control For Init Project
"""

# Libraries
import os
from typing import Callable, List

from src.config import configuration
from src.utils import utils
from src.meta import get_entity
from src.outputs import generate_template

fn_read_json_file = utils.get('inputs').get('read_json_file')
fn_create_path = utils.get('system').get('create_path')
source_generate_path = os.path.join(
    configuration.get('base').get('base_path'),
    configuration.get('base').get('genering_path')
)


def verify_model(entity_model: object) -> Callable:
    """Verify Data of Model"""

    def is_entity(entity: object) -> bool:
        """
        Test to prove if some type is an entity
        """
        return entity.type in entity_model.entities
    return is_entity


def type_data(structure: dict) -> Callable:
    """Type Data Model"""
    def type_mode(_s: object) -> str:
        """
        Maps type names from PrimitiveType to entity
        """
        return structure.get(_s.name, _s.name)
    return type_mode


def read_template(template_path: str) -> Callable:
    """Read Template"""

    def read_module(module: dict) -> dict:
        """Get Module to Template"""
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
        module.update({
            'url_path_generate': os.path.join(
                source_generate_path,
                module.get('configuration_plugin').get('output_path')
            )
        })
        for template in module.get('configuration_plugin').get('templates'):
            output_route = module.get('url_path_generate')
            if 'output_path' in template:
                output_route = os.path.join(
                    output_route,
                    template.get('output_path')
                )
            output_file = 'file'
            if 'fileOutput' in template:
                output_file = os.path.join(
                    output_route,
                    template.get(
                        'fileOutput'
                    ) if template.get('fileOutput') else ''
                )
            template.update({
                'output_route': output_route,
                'output_file_route': '{}.{}'.format(
                    output_file,
                    module.get('configuration_plugin').get('extension')
                )
            })
        return module

    return read_module


def load_configuration_plugins() -> List[dict]:
    """Load a Configuration Plugins"""
    template_configuration = configuration.get('templates').get(
        'template_configuration'
    )
    template_path = configuration.get('templates').get(
        'template_path'
    )
    plugin_configuration = fn_read_json_file(template_configuration)
    return list(
        map(
            read_template(template_path),
            plugin_configuration.get('modules')
        )
    )


def generate_code_plugin(entity: object, plugin: dict):
    """Generate a Code With One plugin"""
    print('--------------------')
    print('Genering - {}'.format(plugin.get('name')))

    print('Creating Directories')
    fn_create_path(source_generate_path)
    fn_create_path(plugin.get('url_path_generate'))

    for template in plugin.get('configuration_plugin').get('templates'):
        print('Build to Specific Template')
        print('Directory')
        fn_create_path(template.get('output_route'))
        print('Genering Code')
        generate_template(
            entity_main=entity,
            verify_model=verify_model(entity),
            type_data=type_data(
                plugin.get('configuration_plugin').get('type_definition')
            ),
            template_path=plugin.get('path_complete'),
            extension=plugin.get('configuration_plugin').get('extension')
        )(template)

    print('--------------------')


def load(entity: str) -> None:
    """Load a Project"""
    entity = os.path.join(
        configuration.get('base').get('base_path'),
        entity
    )
    configuration_plugins = load_configuration_plugins()
    entity = get_entity(entity)

    for module in configuration_plugins:
        generate_code_plugin(entity, module)
