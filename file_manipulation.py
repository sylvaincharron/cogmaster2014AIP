"""
Examples of path manipulation:
1. identify a path withing your hierarchical file organization
Get a file path from a file  i.e.
on windows : in the explorer (window-key + E to launch it), select a file and popy it's path and name
on mac : use the finder (command+N when the finder bar is on top of the screen) to select a file and drag and drop its icone in the terminal
on linux : get a path to a file suing the command line or a gui like nautilus
"""

import os
f="/Users/sc/GitHub/cogmaster2014AIP/file_manipulation.py";
[path,name]=os.path.split(f)
print path
print name

