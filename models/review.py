#!/usr/bin/python3
"""
Defines the class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
	"""
        Review class that inherits from BaseModel
        Attributes:
        place_id (str): The Place id
        user_id (str): The User id
        text (str): Some text for the review
        """
	place_id = ""
	user_id = ""
	text = ""
