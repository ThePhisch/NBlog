"""
Contains the methods to write strings
these will be written to disk by IO (different module) 
"""
from functools import reduce
import json
from typing import Callable, Dict, List, Optional
from blogware.post import Post
from datetime import datetime
from blogware.link import Link


class Writer:
    def __init__(self, link: Link, title: str, posts: List[Post]) -> None:
        self.link = link
        self.title = title
        self.posts = posts
        self.style = "{ width: 60%; margin: auto;}"
        self.numOfPostsInMain = 10
        self.quarterlySplitPosts = self.quarterlySplit()

    def writePage(self, content: str, title: str = "") -> str:
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
        <h1><a href="{self.link.mainU()}">{self.title}</a> {title}</h1>
        <p>Last updated {datetime.now().strftime("%d.%m.%Y %H:%M")}
        <hr>
        {content}
        </body>
        </html> 
        """

    def writeMain(self) -> str:
        """
        Writes the main page. (Needs to be composed with writePage)
        Adds only the first numOfPostsInMain posts.
        some effort went into correctly passing the link destination.
        """
        postpart: str = reduce(
            # Reduce simply concatenates all post strings
            lambda x, y: x + y,
            map(
                # Return post with linkdest for the first numof... posts in array
                lambda x: x.returnPost(linkDest=self.link.postU(x.hash)),
                self.posts[: self.numOfPostsInMain],
            ),
        )
        return postpart + self.archiveListStringProducer()

    def archiveListStringProducer(self) -> str:
        archiveListItems: str = reduce(
            lambda x, y: x + y,
            map(
                lambda x: f"<li><a href='{self.link.quarU(x)}'>Q{x}</a></li>",
                self.quarterlySplitPosts,
            ),
        )
        archive: str = f"""
        <hr>
        <div class="archive">
        <h2>Archive</h2>
        <ul>
        {archiveListItems}
        </ul>
        </div>
        """
        return archive

    def writePosts(self, posts: List[Post]) -> str:
        """
        similar to writeMain (sadly TODO change this into one)
        writes unlimited posts
        """
        postpart: str = reduce(
            # Reduce simply concatenates all post strings
            lambda x, y: x + y,
            map(
                # Return post with linkdest for the first numof... posts in array
                lambda x: x.returnPost(linkDest=self.link.postU(x.hash)),
                posts,
            ),
        )

        return postpart

    def archivePosts(self) -> None:
        """
        Writes the posts.
        TODO make sure to not rewrite the posts that already exist!
        """
        for p in self.posts:
            self.writeIt(self.link.postL(p.hash), self.writePage(p.returnPost()))
        return

    def writeDump(self) -> str:
        """
        Dumps all the posts into a new JSON string.
        """
        dumppart: str = json.dumps(
            list(map(lambda x: x.simplifyForDumping(), self.posts))
        )
        return dumppart

    @staticmethod
    def writeIt(destination: str, towrite: str) -> None:
        with open(destination, "w") as f:
            f.write(towrite)

    def execute(self) -> None:
        self.writeIt(self.link.mainL(), self.writePage(self.writeMain()))
        self.writeIt(self.link.dumpL(), self.writeDump())
        self.archivePosts()
        self.archiveQuarterly()

    def quarterlySplit(self) -> Dict[str, List[Post]]:
        quarters = {}
        for p in self.posts:
            q = str((p.date.month + 2) // 3) + str(p.date.year)
            if q in quarters:
                quarters[q].append(p)
            else:
                quarters[q] = [p]
        return quarters

    def archiveQuarterly(self) -> None:
        for p in self.quarterlySplitPosts:
            self.writeIt(
                self.link.quarL(p),
                self.writePage(
                    self.writePosts(self.quarterlySplitPosts[p]) + self.archiveListStringProducer(),
                    f"Archive page for Q{p}",
                ),
            )
        return
