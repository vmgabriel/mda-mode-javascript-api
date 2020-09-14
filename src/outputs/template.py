"""
Module for Generate Template
"""

# Libraries
from os.path import join
from typing import Callable
import jinja2


def generate_template_with_entity(
        entity_main: object,
        verify_model: Callable,
        type_data: Callable,
        template_path: str,
        extension: str
) -> Callable:
    """Generate Template with Entity Defined"""
    def generate_with_template(template_def: dict) -> None:
        """Generate With Template"""
        jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_path),
            trim_blocks=True,
            lstrip_blocks=True
        )

        jinja_env.tests['entity'] = verify_model
        jinja_env.filters['type_data'] = type_data

        template = jinja_env.get_template(template_def.get('file'))

        for entity in entity_main.entities:
            with open(
                    join(
                        template_def.get('output_route'),
                        '{}.{}'.format(
                            entity.name.lower(),
                            extension
                        )
                    ),
                    'w'
            ) as f:
                f.write(template.render(entity=entity))

    return generate_with_template
