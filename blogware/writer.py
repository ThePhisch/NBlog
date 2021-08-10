"""
Contains the methods to actually write the files to disk
"""
from datetime import datetime


class Writer:
    def __init__(self, loc, title) -> None:
        self.loc = loc
        self.title = title

        self.mainloc = loc + "main.html"

    def writeMain(self) -> None:
        start = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{self.title}</title>
    <style>
    body {{
        width: 60%;
        margin: auto;
    }}
    </style>
</head>
<body>    
    """
        toppart = f"""
<h1>{self.title}</h1>
<p>Last updated {datetime.now().strftime("%d.%m.%Y %H:%M")}
<hr>
"""
        end = f"""
</body>
</html>
    """
        with open(self.mainloc, "w") as f:
            f.write(start)
            f.write(toppart)
            f.write(end)
