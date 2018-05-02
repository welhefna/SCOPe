SCOPe Module Repository
========================

MoDB module is a custom python module to handle mongodb database dynamic queries.
SCOPe module is custom python module to parse .LOC file.


Usage
--------------
	
	from scope import scopeparse as scope_handler

Example
---------------

	try:
		# scope parser initialization	
		p = Parser('/home/welhefna/scope2.06New/newAnalysis/NewDataSetsFragments/fragments/fragments/40/L7/939/7/0.1/shift/aa/FRAG/d2aama1.LOC')

	except :
		#exception handler
		print "Exception is raised !", sys.exc_info()
	else:
		print p.fragments
		print p.fragments_frequency		# print fragments and frequencey of each fragment
		print p.fragments_length		# print length of each fragment
		print p.number_of_residues		# print number of residues
		print p.gaps				# print list of gaps 
		print p.range				# print start , end range of residues
		print p.get_all_fragments_information() # print all fragments information
		

Setup
---------------
	
	python setup.y

