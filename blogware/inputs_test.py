import unittest
from post import Post
import inputs
import json


class testInputs(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        self.jsonIn: str = r'[{"title": "interesting post", "content": "oh hi!\n*you are cute*", "datetime": "20.08.2021 08:34", "hash": "1cc2335c"}]'
        self.putIn: dict = json.loads(self.jsonIn)[0]

    def test_makePostFromJSON(self) -> None:
        p: Post = inputs.makePostFromJSON(self.putIn)

        self.assertEqual(p.title, self.putIn["title"])
        self.assertEqual(p.content, self.putIn["content"])
        self.assertEqual(p.date.strftime("%d.%m.%Y %H:%M"), self.putIn["datetime"])
        self.assertEqual(p.hash, self.putIn["hash"])

    def text_processOldPosts(self) -> None:
        arr: list[Post] = inputs.processOldPosts("tests/dumps.json")
        self.assertListEqual(arr, [inputs.makePostFromJSON(self.putIn)])

