"""
IO, especiall for the input blog files
"""

from io import TextIOWrapper
from typing import List
from blogware.post import Post
from datetime import datetime
import glob
from hashlib import blake2b


def makePostFromText(loc: str) -> Post:

    content: str
    title: str = loc.split("/")[-1][:-4]
    dt: datetime = datetime.now()
    with open(loc, "r", encoding="utf-8") as file:
        content = file.read()

    h: blake2b = blake2b(digest_size=4)
    h.update(f"{content}{title}{dt.strftime('%H:%M')}".encode())
    hash: str = h.hexdigest()

    new: Post = Post(title=title, date=dt, content=content, hash=hash)

    return new


def processNewPosts(searchdir: str) -> List[Post]:
    """
    Creates a list with the new posts, this list can later
    be merged with the posts that already exist.

    params
    : searchdir string naming the directory to search

    outputs
    : list containing the new posts
    """
    return list(map(makePostFromText, glob.glob(f"{searchdir}/*.txt")))
