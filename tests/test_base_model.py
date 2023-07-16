#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
	def test_attributes(self):
    	my_model = BaseModel()
    	my_model.name = "My First Model"
    	my_model.my_number = 89
    	self.assertTrue(hasattr(my_model, 'id'))
    	self.assertTrue(hasattr(my_model, 'created_at'))
    	self.assertTrue(hasattr(my_model, 'updated_at'))
    	self.assertTrue(hasattr(my_model, 'name'))
    	self.assertTrue(hasattr(my_model, 'my_number'))
    	self.assertEqual(my_model.name, "My First Model")
    	self.assertEqual(my_model.my_number, 89)

	def test_str_method(self):
    	my_model = BaseModel()
    	self.assertEqual(
        	str(my_model), "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
    	)

	def test_save_method(self):
    	my_model = BaseModel()
    	old_updated_at = my_model.updated_at
    	my_model.save()
    	self.assertNotEqual(old_updated_at, my_model.updated_at)

	def test_to_dict_method(self):
    	my_model = BaseModel()
    	my_model.name = "My First Model"
    	my_model.my_number = 89
    	obj_dict = my_model.to_dict()
    	self.assertEqual(obj_dict['__class__'], 'BaseModel')
    	self.assertEqual(obj_dict['name'], "My First Model")
    	self.assertEqual(obj_dict['my_number'], 89)
    	self.assertEqual(obj_dict['created_at'], my_model.created_at.isoformat())
    	self.assertEqual(obj_dict['updated_at'], my_model.updated_at.isoformat())


if __name__ == '__main__':
	unittest.main()
