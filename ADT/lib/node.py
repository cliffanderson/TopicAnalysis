# A doubly- or singly-linked Node for use in linked ADTs
class Node:
	# data: The data to store
	# previous: The previous node in the chain
	# next: The next node in a chain
	def __init__(self, data, previous=None, next=None):
		self.data = data
		self.previous = previous
		self.next = next
	
	# Get the data of the node
	def get_data(self):
		return self.data
	
	# Set the next node in the chain
	def set_next(self, next):
		self.next = next
	
	# Get the next node in the chain
	def get_next(self):
		return self.next
		
	# Set the previous node in the chain
	def set_previous(self, previous):
		self.previous = previous
	
	# Get the previous node in the chain
	def get_previous(self):
		return self.previous