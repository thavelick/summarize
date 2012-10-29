import doctest 
from glob import glob
import os.path

paths = glob('test/*.doctest')

for file in paths:
	doctest.testfile(file)