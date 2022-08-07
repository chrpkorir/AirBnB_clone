#!/usr/bin/python3
"""Module city.py
City Class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class representing city."""
    state_id = ""
    name = ""
