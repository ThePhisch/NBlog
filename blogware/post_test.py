from datetime import datetime
import unittest
from post import Post


class testPost(unittest.TestCase):
    def setUp(self) -> None:
        self.title: str = "Testing post"
        self.content: str = "Testing content"
        self.p: Post = Post(self.title, self.content)
        self.date: datetime = datetime.now()

    def test_simplifyForDumping(self) -> None:
        """
        Test whether the outputted dictionary suits the covered
        """
        dumped: dict = self.p.simplifyForDumping()
        self.assertEqual(self.title, dumped["title"])
        self.assertEqual(self.content, dumped["content"])
        self.assertEqual(self.date.strftime("%d.%m.%Y %H:%M"), dumped["datetime"])
        # hash cannot be asserted

    def test_parsingConstructor(self) -> None:
        """
        Test whether the alternative constructor works
        Assuming simplifyForDumping works
        """
        args: dict = self.p.simplifyForDumping()
        altp: Post = Post.parsingConstructor(**args)
        self.assertEqual(self.p.title, altp.title)
        self.assertEqual(self.p.content, altp.content)
        self.assertEqual(
            self.p.date.strftime("%d.%m.%Y %H:%M"), altp.date.strftime("%d.%m.%Y %H:%M")
        )
        self.assertEqual(self.p.hash, altp.hash)

    def tearDown(self) -> None:
        del self.p


if __name__ == "__main__":
    unittest.main(verbosity=2)
