"""
This is the main script to be executed.
It calls on the blogware package for the methods.
"""

from blogware.writer import Writer
from blogware.post import Post
import blogware.inout

LOCATION: str = "output/"
DUMPFILE: str = "dump.json"
TITLE: str = "NBlog"
INPUTS: str = "input/"

if __name__ == "__main__":
    print("running Nblog!")
    writer = Writer(LOCATION, TITLE, blogware.inout.processAllPosts(INPUTS, LOCATION + DUMPFILE))
    writer.execute()
    blogware.inout.deleteInputs(INPUTS)
