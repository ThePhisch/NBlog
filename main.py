"""
This is the main script to be executed.
It calls on the blogware package for the methods.
"""

from blogware.writer import Writer
from blogware.post import Post
import blogware.inputs

LOCATION = "output/"
TITLE = "NBlog"
INPUTS = "input/"

if __name__ == "__main__":
    print("running Nblog!")
    writer = Writer(LOCATION, TITLE)
    writer.execute(blogware.inputs.processNewPosts(INPUTS))
