"""
This is the main script to be executed.
It calls on the blogware package for the methods.
"""

from blogware import writer

LOCATION = "output/"

if __name__ == "__main__":
    print("running Nblog!")
    writer.writeMain(LOCATION)
