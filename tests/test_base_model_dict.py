#!/usr/bin/python3

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
	def test_from_dict_method(self):
    	my_model = BaseModel()
    	my_model.name = "My_First_Model"
    	my_model.my_number = 89
    	my_model_dict = my_model.to_dict()
    	my_new_model = BaseModel(**my_model_dict)
    	self.assertEqual(my_model.id, my_new_model.id)
    	self.assertEqual(my_model.created_at, my_new_model.created_at)
    	self.assertEqual(my_model.updated_at, my_new_model.updated_at)
    	self.assertEqual(my_model.name, my_new_model.name)
    	self.assertEqual(my_model.my_number, my_new_model.my_number)


if __name__ == '__main__':
	unittest.main()
