"""
Module for Use of Conversor data
"""

# Libraries
import uuid


def generate_uuid_4(_d: str) -> str:
    """Generate a New UUID 4"""
    return uuid.uuid4()


conversors = {
    'generate_uuid_4': generate_uuid_4,
}
