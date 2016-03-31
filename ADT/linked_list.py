import os
import sys
lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
sys.path.append(lib_dir)
from node import Node

class LinkedList:
	
	def __init__(self):
		# Create head with None data
		self.head = Node(None)
		self.size = 0
		
	def add(self):
		return 0
		
	def get_size(self):
		return self.size