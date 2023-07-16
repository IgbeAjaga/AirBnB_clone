#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import os
import sys
from models import storage
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
	"""Unit tests for console.py"""

	def setUp(self):
    	"""Set up the test environment"""
    	self.console = HBNBCommand()

	def tearDown(self):
    	"""Tear down the test environment"""
    	self.console = None

	def test_help(self):
    	"""Test the 'help' command"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("help")
        	self.assertIn("Documented commands (type help <topic>):", output.getvalue())

	def test_quit(self):
    	"""Test the 'quit' command"""
    	with self.assertRaises(SystemExit):
        	self.console.onecmd("quit")

	def test_emptyline(self):
    	"""Test an empty command"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("")
        	self.assertEqual("", output.getvalue().strip())

	def test_create(self):
    	"""Test the 'create' command"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("create BaseModel")
        	self.assertIn("b'", output.getvalue())

	def test_show(self):
    	"""Test the 'show' command"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("create BaseModel")
        	obj_id = output.getvalue().strip()
        	self.console.onecmd(f"show BaseModel {obj_id}")
        	self.assertIn(obj_id, output.getvalue())

	def test_destroy(self):
    	"""Test the 'destroy' command"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("create BaseModel")
        	obj_id = output.getvalue().strip()
        	self.console.onecmd(f"destroy BaseModel {obj_id}")
        	self.console.onecmd(f"show BaseModel {obj_id}")
        	self.assertEqual("** no instance found **", output.getvalue().strip())

	def test_all(self):
    	"""Test the 'all' command"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("create BaseModel")
        	self.console.onecmd("create User")
        	self.console.onecmd("all")
        	self.assertIn("BaseModel", output.getvalue())
        	self.assertIn("User", output.getvalue())

	def test_update(self):
    	"""Test the 'update' command"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("create BaseModel")
        	obj_id = output.getvalue().strip()
        	self.console.onecmd(f"update BaseModel {obj_id} name 'New Name'")
        	self.console.onecmd(f"show BaseModel {obj_id}")
        	self.assertIn("'name': 'New Name'", output.getvalue())

	def test_count(self):
    	"""Test the 'count' command"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("create BaseModel")
        	self.console.onecmd("create User")
        	self.console.onecmd("count BaseModel")
        	self.assertIn("1", output.getvalue())
        	self.console.onecmd("count User")
        	self.assertIn("1", output.getvalue())

	def test_all_with_class_name(self):
    	"""Test the 'all' command with class name"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("create BaseModel")
        	self.console.onecmd("create User")
        	self.console.onecmd("all User")
        	self.assertIn("User", output.getvalue())
        	self.assertNotIn("BaseModel", output.getvalue())

	def test_show_invalid_id(self):
    	"""Test the 'show' command with invalid ID"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("show BaseModel invalid_id")
        	self.assertEqual("** no instance found **", output.getvalue().strip())

	def test_destroy_invalid_id(self):
    	"""Test the 'destroy' command with invalid ID"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("destroy BaseModel invalid_id")
        	self.assertEqual("** no instance found **", output.getvalue().strip())

	def test_update_invalid_id(self):
    	"""Test the 'update' command with invalid ID"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("update BaseModel invalid_id name 'New Name'")
        	self.assertEqual("** no instance found **", output.getvalue().strip())

	def test_update_no_attr_value(self):
    	"""Test the 'update' command without attribute value"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("create BaseModel")
        	obj_id = output.getvalue().strip()
        	self.console.onecmd(f"update BaseModel {obj_id} name")
        	self.console.onecmd(f"show BaseModel {obj_id}")
        	self.assertEqual("'name': ''", output.getvalue().strip())

	def test_update_with_dictionary(self):
    	"""Test the 'update' command with dictionary representation"""
    	with patch('sys.stdout', new=StringIO()) as output:
        	self.console.onecmd("create BaseModel")
        	obj_id = output.getvalue().strip()
        	self.console.onecmd(f"update BaseModel {obj_id} {{'name': 'New Name'}}")
        	self.console.onecmd(f"show BaseModel {obj_id}")
        	self.assertIn("'name': 'New Name'", output.getvalue())

	
if __name__ == '__main__':
	unittest.main()

