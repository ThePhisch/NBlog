from datetime import datetime
import unittest
from post import Post

"""

NOTE

the hash needs to be persistant

"""

class testPost(unittest.TestCase):
    def setUp(self) -> None:
        self.title: str = "Testing post"
        self.content: str = "Testing content"
        self.p: Post = Post(self.title, self.content)
        self.date: datetime = datetime.now()

    def test_returnPost(self) -> None:
        """
        Test whether the outputted dictionary suits the covered 
        """
        dumped: dict = self.p.simplifyForDumping()
        self.assertDictEqual(
            dumped,
            {
                "title": self.title,
                "content": self.content,
                "datetime": self.date.strftime("%d.%m.%Y %H:%M"),
            },
        )

    def tearDown(self) -> None:
        del self.p


if __name__ == "__main__":
    unittest.main(verbosity=2)
