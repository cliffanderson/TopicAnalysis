import os
import sys
lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ADT')
sys.path.append(lib_dir)

# Import all ADTs
from linked_list import LinkedList


linked_list = LinkedList()
print(linked_list.get_size())
