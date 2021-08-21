"""
This is the main script to be executed.
It calls on the blogware package for the methods.
"""

from blogware.link import Link
from blogware.writer import Writer
from blogware.post import Post
import blogware.inout

LOCATION: str = "output/"
DUMPFILE: str = "dump.json"
TITLE: str = "NBlog"
INPUTS: str = "input/"

locs = {
    "LOCATION": "output",
    "DUMPFILE": "output/dump.json",
    "MAINFILE": "output/main.html",
    "INPUTS": "input",
    "ARCHIVEQ": "output/q",
    "ARCHIVEP": "output/p",
}

# NOTE if you deploy this, make sure to set the deploy=True flag in link
if __name__ == "__main__":
    print("running Nblog!")
    link = Link(locs, "blog.screamsocial.de", deploy=False)
    writer = Writer(
        link, TITLE, blogware.inout.processAllPosts(link.inputsL(), link.dumpL())
    )
    writer.execute()
    blogware.inout.deleteInputs(INPUTS)

    writer.quarterlySplit()