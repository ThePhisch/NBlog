"""
Contains the methods to write strings
these will be written to disk by IO (different module) 
"""
from functools import reduce
import json
from blogware.post import Post
from datetime import datetime


class Writer:
    def __init__(self, loc, title, posts: list[Post]) -> None:
        self.loc = loc
        self.title = title
        self.posts = posts
        self.mainloc = loc + "main.html"
        self.dumploc = loc + "dump.json"
        self.style = "{ width: 60%; margin: auto;}"
        self.numOfPostsInMain = 10

    def writePage(self, content: callable) -> str:
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{self.title}</title>
            <style>
            body {self.style}
            </style>
        </head>
        <body>
        <h1>{self.title}</h1>
        <p>Last updated {datetime.now().strftime("%d.%m.%Y %H:%M")}
        <hr>
        {content()}
        </body>
        </html> 
        """

    def writeMain(self) -> str:
        """
        Writes the main page. (Needs to be composed with writePage)
        Adds only the first numOfPostsInMain posts.
        """
        postpart: str = reduce(
            lambda x, y: x + y, map(lambda x: x.returnPost(), self.posts[:self.numOfPostsInMain])
        )
        return postpart

    def writeDump(self) -> str:
        """
        Dumps all the posts into a new JSON string.
        """
        dumppart: str = json.dumps(
            list(map(lambda x: x.simplifyForDumping(), self.posts))
        )
        return dumppart

    # TODO: move this method to inout (?)
    @staticmethod
    def writeIt(destination: str, towrite: str) -> None:
        with open(destination, "w") as f:
            f.write(towrite)

    def execute(self) -> None:
        self.writeIt(self.mainloc, self.writePage(self.writeMain))
        self.writeIt(self.dumploc, self.writeDump())
