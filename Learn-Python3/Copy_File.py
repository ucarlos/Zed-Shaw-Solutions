import sys
from sys import argv
import os

script, from_file, to_file = argv

#Check if either file exists
check_from = os.path.exists(from_file)
check_to = os.path.exists(to_file)

if not (check_from and check_to):
    sys.stderr.write("One of your arguments does not exist. Abort.\n")
    sys.exit(1)


print(f"Copying {from_file} to {to_file}")
