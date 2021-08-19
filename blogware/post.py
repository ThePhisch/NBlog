"""
Contains the models to save and interpret posts,
including markdown formatting
"""

from datetime import datetime
from hashlib import blake2b
import markdown2
import json


class Post:
    def __init__(self, title, content) -> None:
        self.title: str = title
        self.content: str = content

        self.date: datetime = datetime.now()
        self.hash = self.hashcalc(
            self.content + self.title + self.date.strftime("%H:%M")
        )

    """
    NOTE
    create additional constructor (maybe with a classmethod)
    that allows to parse the saved post data, in particular
    this method needs to be able take an old hash
    """

    @staticmethod
    def hashcalc(tohash: str) -> str:
        h: blake2b = blake2b(digest_size=4)
        h.update(tohash.encode())
        return h.hexdigest()

    @staticmethod
    def markdowning(tomarkdown: str) -> str:
        return markdown2.markdown(tomarkdown)

    def returnPost(self) -> str:
        postString: str = f"""
<div id={self.hash} class="Post">
    <h4>{self.title}, {self.date.strftime("%d.%m.%Y %H:%M")}</h4>
    {self.markdowning(self.content)}
</div>
        """
        return postString

    def simplifyForDumping(self) -> dict:
        return {
            "title" : self.title,
            "content" : self.content,
            "datetime" : self.date.strftime("%d.%m.%Y %H:%M")
        }
    
