"""
IO, especiall for the input blog files
"""

from io import TextIOWrapper
from typing import List
from blogware.post import Post
import glob
import json


def processNewPosts(searchdir: str) -> List[Post]:
    """
    Creates a list with the new posts, this list can later
    be merged with the posts that already exist.

    params
    : searchdir string naming the directory to search

    outputs
    : list containing the new posts
    """

    return list(map(loadTextAndMakePost, glob.glob(f"{searchdir}/*.txt")))


def processOldPosts(loc: str) -> List[Post]:
    """
    Creates a list with the old posts

    params
    : searchloc string naming the file to open and parse

    outputs
    : list containing the old posts
    """
    content: str = loadFile(loc)

    return list(map(makePostFromJSON, json.loads(content)))


def loadFile(loc: str) -> str:
    content: str
    with open(loc, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def makePostFromJSON(jdata: dict) -> Post:
    return Post.parsingConstructor(**jdata)


def loadTextAndMakePost(loc: str) -> Post:

    content: str = loadFile(loc)
    title: str = loc.split("/")[-1][:-4]

    new: Post = Post(title, content)

    return new
