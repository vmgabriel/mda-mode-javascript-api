"""
Module for Generate Template
"""

# Libraries
from os.path import join
from typing import Callable
import jinja2

# Handlers
from src.outputs.handlers import handlers

def generate_template_with_entity(
        entity_main: object,
        modules: dict,
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

        jinja_env.tests['entity'] = handlers.get('verify_model')(entity_main)
        jinja_env.filters['type_data'] = handlers.get('type_data')(modules)

        for name_filter, value_filter in handlers.get('filters').items():
            jinja_env.tests[name_filter] = value_filter

        for name_conversor, value_conversor in handlers.get(
                'conversors'
        ).items():
            jinja_env.filters[name_conversor] = value_conversor

        template = jinja_env.get_template(template_def.get('file'))

        is_one_file = template_def.get('oneFile') if \
            template_def.get('oneFile') else False

        if is_one_file:
            print('File Output - {}'.format(
                template_def.get('output_file_route')
            ))
            file_output = template_def.get('output_file_route') \
                if template_def.get('output_file_route') else join(
                    template_def.get('output_route'),
                    'file.{}'.format(
                        extension
                    )
                )
            with open(file_output, 'w') as _f:
                _f.write(template.render(entities=entity_main.entities))
        else:
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
                ) as _f:
                    _f.write(template.render(entity=entity))

    return generate_with_template
