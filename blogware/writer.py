"""
Contains the methods to actually write the files to disk
"""

def writeMain(loc) -> None:
    with open(loc + "main.html", "w") as f:
        f.write("Henlo (:")