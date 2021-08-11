"""
Contains the methods to actually write the files to disk
"""
from functools import reduce
from blogware.post import Post
from datetime import datetime


class Writer:
    def __init__(self, loc, title) -> None:
        self.loc = loc
        self.title = title

        self.mainloc = loc + "main.html"

    def writeMain(self, posts: list[Post]) -> None:
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
            lambda x, y: x + y, map(lambda x: self.writePost(x), posts)
        )

        end: str = f"""
</body>
</html>
    """
        # TODO: make this entire function export a string, write this string with function from somewhere else
        with open(self.mainloc, "w") as f:
            f.write(start)
            f.write(toppart)
            f.write(postpart)
            f.write(end)

    def writePost(self, post: Post) -> str:
        out = f"""
<div id={post.hash} class='Post'>
<h4>{post.title}, {post.date.strftime("%d.%m.%Y")}</h4>
<p>{post.content}</p>
</div>
        """
        return out
