"""
Contains the methods to actually write the files to disk
"""
from functools import reduce
import json
from blogware.post import Post
from datetime import datetime


class Writer:
    def __init__(self, loc, title) -> str:
        self.loc = loc
        self.title = title

        self.mainloc = loc + "main.html"
        self.dumploc = loc + "dump.json"

    def writeMain(self) -> None:
        start: str = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{self.title}</title>
    <style>
    body {{
        width: 60%;
        margin: auto;
    }}
    </style>
</head>
<body>    
    """
        toppart: str = f"""
<h1>{self.title}</h1>
<p>Last updated {datetime.now().strftime("%d.%m.%Y %H:%M")}
<hr>
"""

        postpart: str = reduce(
            lambda x, y: x + y, map(lambda x: x.returnPost(), self.posts)
        )

        end: str = f"""
</body>
</html>
    """
        return start + toppart + postpart + end

    def writeDump(self) -> str:
        dumppart: str = json.dumps(
            list(map(lambda x: x.simplifyForDumping(), self.posts))
        )
        return dumppart

    @staticmethod
    def writeIt(destination: str, towrite: str) -> None:
        with open(destination, "w") as f:
            f.write(towrite)

    def execute(self, posts: list[Post]) -> None:
        self.posts = posts
        self.writeIt(self.mainloc, self.writeMain())
        self.writeIt(self.dumploc, self.writeDump())
