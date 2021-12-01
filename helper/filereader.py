class Filereader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "r")
        self._content = []

    def readline(self):
        return self.file.readline()

    def get_content(self):
        if not self.file:
            return []
        if not self._content:
            self._content = self.file.read().splitlines()
        return self._content

    def close(self):
        if self.file:
            self.file.close()
