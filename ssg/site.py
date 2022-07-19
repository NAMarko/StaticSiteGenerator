from pathlib import Path

class Site():
    def __init__(self, source, dest):
        source = Path(self.source)
        dest = Path(self.dest)

    def create_dir(self, path):
        directory = (self.dest,"/",relative_to(self.source))
        print(directory) 
        directory.mkdir( parents=True, exist_ok=True )

    def build():
        self.dest.mkdir( parents=True, exist_ok=True )
        for path in self.source.rglob("*"):
            if (path.isdir):
                create_dir(path)

    