"""
Contains the models to save and interpret posts,
including markdown formatting
"""

from datetime import datetime
from hashlib import blake2b
import markdown2


class Post:
    def __init__(self, title, content, parsing: bool = False) -> None:
        self.title: str = title
        self.content: str = content

        if not parsing:
            self.date: datetime = datetime.now()
            self.hash = self.hashcalc(
                self.content + self.title + self.date.strftime("%H:%M")
            )

    @classmethod
    def parsingConstructor(cls, **kwargs) -> "Post":
        p: Post = cls(kwargs["title"], kwargs["content"], parsing=True)
        p.date = datetime.strptime(kwargs["datetime"], "%d.%m.%Y %H:%M")
        p.hash = kwargs["hash"]
        return p

    @staticmethod
    def hashcalc(tohash: str) -> str:
        h: blake2b = blake2b(digest_size=4)
        h.update(tohash.encode())
        return h.hexdigest()

    @staticmethod
    def markdowning(tomarkdown: str) -> str:
        return markdown2.markdown(tomarkdown)

    def returnPost(self, linkDest: str = "") -> str:
        postString: str = f"""
        <div id={self.hash} class="Post">
        <h4><a href="{linkDest}">[l]</a> {self.title}, {self.date.strftime("%d.%m.%Y")}</h4>
        {self.markdowning(self.content)}
        </div>
        """
        return postString

    def simplifyForDumping(self) -> dict:
        return {
            "title": self.title,
            "content": self.content,
            "datetime": self.date.strftime("%d.%m.%Y %H:%M"),
            "hash": self.hash,
        }
