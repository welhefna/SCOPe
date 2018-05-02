# -*- coding: utf-8 -*-

import doctest
from context import scope as scope_handler
	

def basic_methods():
	"""Basic methods operations
	
	>>> p = scope_handler.SCOPeParser('tests/static/d2aama1_7.LOC')
	>>> print p.fragments_length		# print length of each fragment
	7
	>>> print p.number_of_residues		# print number of residues
	119
	>>> print p.gaps				# print list of gaps 
	[(0, 9), (44, 56), (144, 156), (162, 174), (267, 279), (267, 279)]
	>>> print p.range				# print start , end range of residues
	(0, 283)
	
	"""


if __name__ == '__main__':
	doctest.testmod()
