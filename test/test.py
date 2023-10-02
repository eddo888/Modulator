#!/usr/bin/env python3

# PYTHON_ARGCOMPLETE_OK

import io, sys, os

sys.path.insert(0, '..')
	
from Modulated.Warbeler import Warbeler

warbler = Warbeler(colour=True)

warbler.sing(files=os.listdir()+['.','..','../bin'])


