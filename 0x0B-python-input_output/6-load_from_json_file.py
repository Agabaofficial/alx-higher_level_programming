#!/usr/bin/python3
import json
"""
function that creates an Object from a "JSON file".
"""


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, 'r') as f:
        return json.loads(f.read())
