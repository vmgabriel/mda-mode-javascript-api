
"""
Package to Configuration the app
"""

from src.config.templates import configuration as template_configuration
from src.config.base import configuration as base_configuration

configuration = {
    "base": base_configuration,
    "templates": template_configuration,
}
