"""
Configuration for templates in Javascript
"""

# Libraries
import os

configuration = {
    "template_path": os.path.join(os.getcwd(), 'templates'),
    "template_configuration": os.path.join(
        os.getcwd(),
        'templates',
        'plugins.json'
    ),
}
