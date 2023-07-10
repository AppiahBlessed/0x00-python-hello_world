#!/usr/bin/python3
from io import StringIO
import sys

zen = StringIO()
sys.stdout == zen

import this

sys.stdout = sys.__stdout__
zenout = zen.getvalue()
print(zenout)
