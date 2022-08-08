#!/usr/bin/python3

"""class User that inherits from BaseModel."""

from models.base_model import BaseModel
import models


class User(BaseModel):
    """Public class attributes:"""
    """email, password, first name, last name: empty strings."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
