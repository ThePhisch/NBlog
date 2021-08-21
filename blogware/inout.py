"""
IO, especiall for the input blog files
"""
from functools import reduce
from typing import List
from blogware.post import Post
from datetime import datetime
import glob
import json
import os


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

def processAllPosts(searchdir: str, loc: str) -> List[Post]:
    """
    Return sorted list of all old and new posts
    """
    postList: List[Post] = processNewPosts(searchdir) + processOldPosts(loc)
    return sorted(postList, key=lambda x: x.date, reverse=True)

def loadFile(loc: str) -> str:
    content: str
    with open(loc, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def makePostFromJSON(jdata: dict) -> Post:
    return Post.parsingConstructor(**jdata)


def loadTextAndMakePost(loc: str) -> Post:

    content: str = loadFile(loc)
    splitcontent = content.split("\n")

    new: Post = Post(splitcontent[0], reduce(lambda x, y: x + "\n" + y, splitcontent[1:]))

    return new

def deleteInputs(searchdir: str) -> None:
    for file in glob.glob(f"{searchdir}/*.txt"):
        os.remove(file)