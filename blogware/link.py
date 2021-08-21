"""
Create link addresses
Differentiate between deploy mode (URL) and development/testing (absolute on device)
"""
from pathlib import Path


class Link:
    def __init__(self, locs: dict, url: str = "", deploy: bool = False) -> None:
        self.deploy = deploy
        self.url = url

        self.basePath: Path = Path.cwd()
        self.locs = locs

    def mainL(self) -> str:
        return str(self.basePath / self.locs["MAINFILE"])

    def postL(self, hash: str) -> str:
        filename: str = hash + ".html"
        return str(self.basePath / self.locs["ARCHIVEP"] / filename)

    def quarL(self, quarterId: str) -> str:
        filename: str = quarterId + ".html"
        return str(self.basePath / self.locs["ARCHIVEQ"] / filename)

    def dumpL(self) -> str:
        return str(self.basePath / self.locs["DUMPFILE"])

    def postU(self, hash: str) -> str:
        if not self.deploy:
            return self.postL(hash)
        else:
            return self.url + f"/output/p/{hash}.html" 

    def mainU(self) -> str:
        if not self.deploy:
            return self.mainL()
        else:
            return self.url

    def quarU(self, quarterId: str) -> str:
        if not self.deploy:
            return self.quarL(quarterId)
        else:
            return self.url + f"/output/q/{quarterId}.html"

    def inputsL(self) -> str:
        return str(self.basePath / self.locs["INPUTS"])
