import unittest
from blogware.post import Post
import inout
import json


class testInputs(unittest.TestCase):
    def setUp(self) -> None:
        self.jsonIn: str = r'[{"title": "interesting post", "content": "oh hi!\n*you are cute*", "datetime": "20.08.2021 10:31", "hash": "1cc2335c"}]'
        self.putIn: dict = json.loads(self.jsonIn)[0]

    def test_makePostFromJSON(self) -> None:
        p: Post = inout.makePostFromJSON(self.putIn)

        self.assertEqual(p.title, self.putIn["title"])
        self.assertEqual(p.content, self.putIn["content"])
        self.assertEqual(p.date.strftime("%d.%m.%Y %H:%M"), self.putIn["datetime"])
        self.assertEqual(p.hash, self.putIn["hash"])

    def test_processOldPosts(self) -> None:
        arr: list[Post] = inout.processOldPosts("tests/dump.json")

        self.assertEqual(len(arr), 1)

        self.assertEqual(arr[0].title, self.putIn["title"])
        self.assertEqual(arr[0].content, self.putIn["content"])
        self.assertEqual(arr[0].date.strftime("%d.%m.%Y %H:%M"), self.putIn["datetime"])
        self.assertEqual(arr[0].hash, self.putIn["hash"])