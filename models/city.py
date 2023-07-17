#!/usr/bin/python3
"""Defines the class City"""
from models.base_model import BaseModel


class City(BaseModel):
	"""City class that inherits from BaseModel.
        Attributes:
        state_id (str): state id
        name (str): The city name
        """
	state_id = ""
	name = ""
